DROP TABLE IF EXISTS mimiciv_derived.ns_db_cohort; CREATE TABLE mimiciv_derived.ns_db_cohort AS

with neur_mimiciv_0 as (
    SELECT distinct ad.subject_id, ad.hadm_id
    , pt.gender, TO_TIMESTAMP(CAST(pt.dod AS text), 'YYYY-MM-DD HH24:MI:SS')::timestamp without time zone as deathtime
    , ad.admittime, ad.dischtime
    , icud.admission_age as age, icud.race as ethnicity
    , round(extract(EPOCH from icud.dischtime - icud.admittime)/60.0/60.0/24,2) as los_hospital_day
    , ad.admission_type, pt.anchor_year_group
    FROM `physionet-data.mimiciv_3_1_hosp.admissions` ad
    left join `physionet-data.mimiciv_3_1_icu.icustays` icud
	on icud.subject_id = ad.subject_id
	and icud.hadm_id = ad.hadm_id
	left join `physionet-data.mimiciv_3_1_hosp.patients` pt
	on ad.subject_id = pt.subject_id
    inner join (
        SELECT distinct subject_id, hadm_id FROM `physionet-data.mimiciv_3_1_hosp.transfers`
        where careunit = 'Neuro Surgical Intensive Care Unit (Neuro SICU)'
    ) tf
    on icud.subject_id = tf.subject_id
    and icud.hadm_id = tf.hadm_id
    where icud.admission_age >= 16
)

, neur_mimiciv_1 as (
	select icud.subject_id, icud.hadm_id, los_hospital_day
  , case when deathtime > admittime and deathtime <= dischtime + INTERVAL '1 day' then 1
	else 0 end as death_hosp
  	, case 
    when icud.admission_type in ('AMBULATORY OBSERVATION', 'DIRECT OBSERVATION', 'EU OBSERVATION', 'OBSERVATION ADMIT') then 'OBSERVATION'
    when icud.admission_type in ('ELECTIVE') then 'ELECTIVE'
    when icud.admission_type in ('DIRECT EMER.', 'EW EMER.') then 'EMERGENCY'
    when icud.admission_type in ('SURGICAL SAME DAY ADMISSION', 'URGENT')  then 'URGENT'
    else null end as admission_type
    , icud.ethnicity
    , icud.anchor_year_group
  	, gender, round(age,2) as age
  	, height, weight
	, case when wt.weight > 0 and ht.height > 0 then round(cast((10000 * wt.weight)/(ht.height * ht.height) as numeric),2) -- weight(kg)/height^2(m)
	else null end as bmi
	from neur_mimiciv_0 icud
	left join (
		select icud.subject_id, icud.hadm_id, round(avg(coalesce(weight, weight_admit))::numeric,1) as weight 
		from mimiciv_derived.first_day_weight w
    inner join mimiciv_derived.icustay_detail icud
    on w.stay_id = icud.stay_id
		where coalesce(weight, weight_admit) > 20 -- we think adult weight can not less than 20kg
		and coalesce(weight, weight_admit) < 400
    group by icud.subject_id, icud.hadm_id
	) wt
	on wt.subject_id = icud.subject_id
  and wt.hadm_id = icud.hadm_id
	left join (
		SELECT icud.subject_id, icud.hadm_id, round(avg(height)::numeric,1) as height
    FROM mimiciv_derived.height c
    inner join mimiciv_derived.icustay_detail icud
    on c.stay_id = icud.stay_id
    where c.height != 0
		AND c.height > 120 and c.height < 230
    group by icud.subject_id, icud.hadm_id
	) ht	 
	on ht.subject_id = icud.subject_id
  and ht.hadm_id = icud.hadm_id
)

-- mimic_ns_info
, cohort as (
  select subject_id, hadm_id, gender, age, ethnicity
  , los_hospital_day, admission_type
  , death_hosp, anchor_year_group
  , height, weight, bmi
  from neur_mimiciv_1
)

select *
from cohort
order by subject_id, hadm_id;


select di.subject_id, di.hadm_id, di.icd_code, di.icd_version, did.long_title, di.seq_num 
from mimiciv_hosp.diagnoses_icd di
inner join (
  select distinct subject_id, hadm_id from mimiciv_derived.ns_db_cohort
) sc
on di.subject_id = sc.subject_id
and di.hadm_id = sc.hadm_id
left join mimiciv_hosp.d_icd_diagnoses did 
on di.icd_code = did.icd_code
and di.icd_version = did.icd_version
order by di.subject_id, di.hadm_id, di.seq_num