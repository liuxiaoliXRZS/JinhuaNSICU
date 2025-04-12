import pandas as pd
## 变成英文的是否
YesOrNo = {'是':'Yes','否':'No'}

# df = pd.read_csv('0729v2/Medical_record.csv')
# column_list = ['previous_illness_flag','quit_smoking_flag','previous_surgery_flag','smoke_flag','fertility_flag',
#                'history_blood_transfusion_flag','weight_changed_flag','history_allergy_flag','drink_alcohol_flag',
#                'quit_drinking_flag','menstruation_regular_flag','surgery_flag','dysmenorrhea_flag','menopause_flag',
#                'epidemic_area_contact_flag','operate_flag','laboratory_tests_flag','microbial_culture_flag',
#                'physical_examination_flag','pathological_examination_flag','pathological_cell_bank_record_flag',
#                'clinical_pathway_flag','chemotherapy_flag','endocrine_therapy_flag','targeted_therapy_flag']

# for col in column_list:

#     df[col] = df[col].map(YesOrNo).fillna(df[col])

# df.to_csv('0729v3/Medical_record.csv')


## 将年龄变成以年为单位
# df = pd.read_csv('0802v1/Surgical_record_front_page.csv')

# df['age_medical_records_onset'] = df['age_medical_records_onset'].apply(lambda x: int(x/365) if pd.notna(x) else x)
# print(df['age_medical_records_onset'])
# df.to_csv('0729v3/Medical_record.csv')

## 保存要翻译的列的元素
# unique = df['surgery_name_norm'].unique()
# unique_df = pd.DataFrame(unique,columns=['surgery_name_norm'])
# unique_df.to_excel('surgery_name.xlsx',index=False)


# 去除日期信息
# import re
# df = pd.read_csv('0729v3\Medical_record.csv',encoding='gbk')


# # text = '两侧胸廓对称，气管居中。两肺纹理增多，两肺见片状密度增高影，边界模糊。心脏及大血管影位置、形态位于正常范围。两侧横膈光整，两侧肋膈角变钝。较前片2014-1-5进展。'
# def remove_dates(text):
#     # text = re.sub('（临床操作医生：李颖如，卢斌）  联系电话：13429049868','',text)
#     return re.sub(r'\d{4}[-.]\d{1,2}[-.]\d{1,2}|\d{2}[-.]\d{2}|\d{8}', '****-**-**', text)

# df['auxiliary_inspection'] = df['auxiliary_inspection'].apply(lambda x: remove_dates(str(x)) if pd.notna(x) else x)
# df['chief_complaint'] = df['chief_complaint'].apply(lambda x: remove_dates(str(x)) if pd.notna(x) else x)
# df['present_illness'] = df['present_illness'].apply(lambda x: remove_dates(str(x)) if pd.notna(x) else x)
# df['past_history'] = df['past_history'].apply(lambda x: remove_dates(str(x)) if pd.notna(x) else x)
# df['discharge_status'] = df['discharge_status'].apply(lambda x: remove_dates(str(x)) if pd.notna(x) else x)
# df['discharge_instructions'] = df['discharge_instructions'].apply(lambda x: remove_dates(str(x)) if pd.notna(x) else x)
# # print(remove_dates(text))
# df.to_csv('0729v3/Medical_record(rm_privacy).csv',index=False)

df = pd.read_csv('0802v1\Round_records.csv')
gcs_exists = df[df['GCS'].notnull()]

unique_hadm_ids = gcs_exists['subject_id'].nunique()
print(unique_hadm_ids)