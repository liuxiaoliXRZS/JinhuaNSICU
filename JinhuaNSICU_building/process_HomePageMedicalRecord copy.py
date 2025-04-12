import os
import pandas as pd
file_path = "./dataframe_uni_merge/病案首页.csv"
column_list = ["main_diagnosis_flag","discharge_type","medical_payment_type","patient_gender","patient_ethnicity"
,"marital_status"
,"professional"
,"admission_department"
,"discharge_department"
,"abo_blood_type"
,"rh_blood_type"
,"clinical_pathway_status"
,"outpatient_hospital_diagnosis_check"
,"admission_discharge_diagnosis_check"
,"admission_route"
,"discharge_ward"]

result_data = []

df = pd.read_csv(file_path,encoding="utf-8")
for column in column_list:
    # 提取某一列的不重复元素
    column_values = df[column].unique()
    # column_values = df[df[column] != ''][column].unique()

    # 将每一列的数据逐行添加到结果列表
    for value in column_values:
        result_data.append([column, value])

# 创建包含结果数据的DataFrame
result_df = pd.DataFrame(result_data, columns=['column_name', 'value_cn'])

# 将DataFrame保存为CSV文件
output_file_path = 'translation/病案首页_transfer1.csv'
result_df.to_csv(output_file_path, index=False)