"""
Generate a TableOne object from a dataset and save it to an Excel file.
"""
import pandas as pd
from tableone import TableOne

data1 = pd.read_csv('mimic_ns_diagnosis.csv')
data2 = pd.read_csv('inspire_ns_diagnosis.csv')
mimic_hadm_num = data1['hadm_id'].nunique()
inspire_hadm_num = data2['hadm_id'].nunique()

# 将非数值的值映射为数值型
# data['patient_gender_en'] = data['patient_gender_en'].map({'男': 0, '女': 1})
# data['admission_type'] = data['admission_type'].map({'EMERGENCY':1,'URGENT':1}).fillna(0)
# data['admission_route'] = data['admission_route'].map({'急诊':1}).fillna(0)
# 创建TableOne对象并指定分类变量和数值变量
table1 = TableOne(data1, columns=['gender','age','los_hospital_day','admission_type','ethnicity','death_hosp'], 
                 nonnormal=['age','los_hospital_day'],
                 categorical=['gender','ethnicity','admission_type','death_hosp'],
        )
table2 = TableOne(data2, columns=['sex','age','los_hospital_day','admission_type','race','death_hosp'], 
                 nonnormal=['age','los_hospital_day'],
                 categorical=['sex','race','admission_type','death_hosp'],
        )
# 执行统计并打印结果
table1.to_excel("mimic_ns.xlsx")
table2.to_excel("inspire_ns.xlsx")