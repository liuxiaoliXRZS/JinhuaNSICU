import pandas as pd

def remove_columns_from_csv(input_file,output_file,columns_to_remove):
    try:
        df = pd.read_csv(input_file,encoding='utf-8')
    except UnicodeDecodeError:
        df = pd.read_csv(input_file,encoding='gbk')
    df.drop(columns=columns_to_remove,inplace = True)
    df.to_csv(output_file,index=False)

input_file = '0802v1/medical_record.csv'
output_file = '0903v1/medical_record.csv'
#  病历
columns_to_remove = ['admission_status_within24h_hosp','treatment_description_within24h_hosp','discharge_status_within24h_hosp',
                     'death_time_within24h_hosp','death_time_within24h_hosp_base','chief_complaint_within24h_hosp','admission_status_within24h_hosp_base',
                     'treatment_process_description_within24h_hosp','death_cause_within24h_hosp','auxiliary_inspection','present_illness','past_history',
                     'menstrual_history','personal_history','reproductive_history','menopause_age','marriage_childbearing_history','exposure_radioactive_material_flag',
                     'last_menstrual_period','last_menstrual_period_base','family_history','kinship','waistline','hips','admission_status','treatment_process','discharge_status',
                     'discharge_instructions','adverse_event_time','consultation_topic','first_postoperative_course_time','disease_course_details_hospitalization','recording_time_firstcourseillness',
                     'diagnostic_basis_firstcourseillness','medical_record_char_firstcourseillness','differential_diagnosis_firstcourseillness','treatment_plan_firstcourseillness','mdt_clinic_flag',
                     'chief_complaint_op','current_illness_history_op','family_history_op','past_history_op','physical_examination_op','auxiliary_examination_op','treatment_op','suggestions_op',
                     'admittime','dischtime','discharge_doctor_advice_within24h_hosp'
]
#  病案首页
# columns_to_remove = ['total_fees_receivable','admittime','out_pocket_expenses','general_medical_expenses','general_treatment_operation_cost',
#                      'nursing_cost','pathological_diagnosis_cost','laboratory_diagnostic_cost','imaging_diagnosis_cost','clinical_diagnosis_cost',
#                      'nonsurgical_treatment_cost','clinical_physiotherapy_cost','surgical_treatment_cost','anesthesia_cost','surgery_cost','rehabilitation_cost',
#                      'tcm_treatment_cost','clinical_pathway_status','clinical_pathway_status_en','rescues_num','successful_rescues_num','western_medicine_cost',
#                      'antibacterial_drug_cost','chinese_patent_medicine_cost','chinese_herbal_medicine_cost','blood_cost','albumin_products_cost','globulin_product_cost',
#                      'coagulation_factor_products_cost','cytokine_product_cost','medical_material_treatment_cost_per','check_medical_material_cost_per',
#                      'surgery_medical_material_cost_per','other_cost','dischtime'
#                      ]

remove_columns_from_csv(input_file,output_file,columns_to_remove)