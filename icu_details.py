import pandas as pd
"""
This script processes hospital admission records and ICU treatment data to generate a summary table 
containing key metrics such as hospital length of stay (LOS), ICU treatment duration, and patient details.
"""
merged_df = pd.read_csv('0924\medical_record_front_page.csv')

# 计算医院住院时长 (los_hospital)
merged_df['los_hospital'] = ((merged_df['dischtime_base']- merged_df['admittime_base']) / (60 * 24)).round(2)

# 标记住院顺序 (hospstay_seq) 和是否为第一次住院 (first_hosp_stay)
merged_df['hospstay_seq'] = merged_df['admitted_rank']
merged_df['first_hosp_stay'] = merged_df['hospstay_seq'] == 1

# ICU 相关字段
icu_df = pd.read_csv('0924\Orders.csv')
icu_df = icu_df[icu_df['order_content'] == 'ICU单元治疗']
icu_df['starttime_base'] = pd.to_numeric(icu_df['starttime_base'],errors='coerce')
icu_df['endtime_base'] = pd.to_numeric(icu_df['endtime_base'],errors='coerce')
icu_df['icu_time'] = (icu_df['endtime_base'] - icu_df['starttime_base'])
icu_time = (icu_df.groupby('hadm_id')['icu_time'].sum() / (60 * 24)).round(2).reset_index()

merged_df = merged_df.merge(icu_time, on='hadm_id', how='left')
# 填充缺失值（对于没有 ICU 时间的记录，填充为 0）
merged_df['icu_time'] = merged_df['icu_time'].fillna(0)
icustay_detail = merged_df[[
    'subject_id', 'hadm_id', 
    'patient_gender_en', 'age',
    'admittime_base', 'dischtime_base', 'los_hospital', 'discharge_type_en',
    'hospstay_seq', 'first_hosp_stay', 'icu_time',
]]

icustay_detail.to_csv('./OpenCode/icustay_detail.csv', index=False)