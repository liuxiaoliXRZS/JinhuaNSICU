import pandas as pd
import re


input_file = "./dataframe_uni_merge_translated/Medical_record_front_page.csv"
output_file = "./temp/statistic_death.csv"

# 读取CSV文件
df = pd.read_csv(input_file)
# 将入院时间列解析为日期时间格式
df['admittime'] = pd.to_datetime(df['admittime'],format = '%Y%m%d %H:%M:%S')
# 按入院时间降序排序
df = df.sort_values(by='admittime',ascending = False)
print(df)
df.to_csv(output_file,index=False)
# 删除重复ID的行
df = df.drop_duplicates(subset="subject_id", keep="first")
# 根据病人ID筛选数据

df = df[df['discharge_type'] != '死亡'] 
df = df[['subject_id','hadm_id']]
# selected_data = df_unique[['subject_id','patient_gender_en','age','dischtime_base','admission_route','discharge_type']]
# selected_data['age'] = selected_data['age'].apply(lambda x:round(x/365,1))
# selected_data['los_hospital_day'] = selected_data['dischtime_base'].apply(lambda x:round(x/(24*60),2))
# selected_data = selected_data.drop('dischtime_base',axis = 1)
# selected_data['death_hosp'] = selected_data['discharge_type'].apply(lambda x:1 if x =="死亡" else 0)
# selected_data = selected_data.drop('discharge_type',axis = 1)
 # 将DataFrame保存到新的CSV文件
df.to_csv(output_file, index=False)

subjectID_list = df['subject_id'].tolist()

df1 = pd.read_csv('./dataframe_uni_merge_translated/Daily_progress.csv')
df1['charttime'] = pd.to_datetime(df1['charttime'],format = '%Y%m%d %H:%M:%S')
df1 = df1.sort_values(by = 'charttime',ascending= False)
df1.to_csv('statistic_daily_progress_death.csv',index= False)
df1 = df1.drop_duplicates(subset="subject_id", keep="first")
df1 = df1[df1['subject_id'].isin(subjectID_list)]
df1.to_csv('statistic_daily_progress_death.csv',index= False)

keywords = [
'胸外心脏按压',
'肾上腺素',
'去甲肾上腺素',
'心率逐渐下降',
'血压测不出',
'血氧饱和度测不出',
'大剂量多巴胺',
'大剂量血管活性药物',
'心电图呈一直线',
'双瞳孔散大固定',
'心肺复苏',
'心脏电除颤术',
'尸体',
'死亡',
'心脏电复律术',
'病员及家属表示理解并接受',
'表示理解和接受',
'要求出院',
'办理出院',
'要求转院',
'自动出院',
'家属要求'
]

df1 = df1[df1.apply(lambda row:any(keyword in str(row) for keyword in keywords), axis= 1)]
df1 = df1[['subject_id','hadm_id','course_details']]
df1.to_csv('./temp/statistic_death_part1.csv',index=False)

df2 = pd.read_csv('./dataframe_uni_merge_translated/discharge_diagnosis_front_page.csv')
df2 = df2[df2['subject_id'].isin(subjectID_list)]

df2 = df2[df2['disease_outcome'] == '死亡']
df2 = df2[['subject_id','hadm_id','discharge_diagnosis','disease_outcome']]
df2.to_csv('./temp/statistic_death_part2.csv',index=False)

df3 = pd.read_csv('./dataframe_uni_merge_translated/Medical_record.csv')
df3 = df3[df3['subject_id'].isin(subjectID_list)]

df3 = df3[df3['expire_flag'] == '是']
df3 = df3[['subject_id','hadm_id','expire_flag']]
df3.to_csv('./temp/statistic_death_part3.csv',index=False)

df4 = pd.read_csv('./dataframe_uni_merge_translated/Orders.csv')
df4 = df4[df4['subject_id'].isin(subjectID_list)]
df4['starttime'] = pd.to_datetime(df4['starttime'],format = '%Y%m%d %H:%M:%S')
df4 = df4.sort_values(by = 'starttime',ascending= False)
df4 = df4.drop_duplicates(subset="subject_id", keep="first")
keywords = [
'胸外心脏按压',
'肾上腺素',
'去甲肾上腺素',
'心率逐渐下降',
'血压测不出',
'血氧饱和度测不出',
'大剂量多巴胺',
'大剂量血管活性药物',
'心电图呈一直线',
'双瞳孔散大固定',
'心肺复苏',
'心脏电除颤术',
'尸体',
'死亡',
'心脏电复律术',
'病员及家属表示理解并接受',
'表示理解和接受',
'要求出院',
'办理出院',
'要求转院',
'自动出院',
'家属要求'
]

df4 = df4[df4['order_content'].apply(lambda row: any(keyword in str(row) for keyword in keywords))]
df4 = df4[['subject_id','hadm_id','order_content']]
df4.to_csv('./temp/statistic_death_part4.csv',index=False)
bool_list = []
df5 = pd.read_csv('./dataframe_uni_merge_translated/Vital_signs.csv')
df5 = df5[df5['subject_id'].isin(subjectID_list)]
df5['charttime'] = pd.to_datetime(df5['charttime'],format = '%Y%m%d %H:%M:%S')
df5 = df5.sort_values(by = 'charttime',ascending= False)
df5 = df5.drop_duplicates(subset=["subject_id",'subcategory_name'], keep="first")
for row in df5.itertuples():  # 跳过表头，即第一行
    try:
        first_value_str = row.value.split()[0]
        first_value = float(first_value_str)
    except ValueError:
        first_value_str = row.value.split()[0].replace('%','')
        if first_value_str == '测不出' or first_value_str == '.' or first_value_str == '无法测量':
            bool_list.append(False)
            continue
        first_value = float(first_value_str)
    if row.subcategory_name == '收缩压' and first_value < 60:
        bool_list.append(True)
    elif row.subcategory_name == '心率' and first_value < 30:
        bool_list.append(True)
    elif row.subcategory_name == '血氧饱和度'and first_value < 85:
        bool_list.append(True)
    else:
        bool_list.append(False)
df5 = df5[bool_list]
df5 = df5[['subject_id','hadm_id','subcategory_name','value']]
df5.to_csv('./temp/statistic_death_part5.csv',index=False)

# want = pd.DataFrame(columns=['subject_id','hadm_id','course_details','disease_outcome','expire_flag','order_content','subcategory_name','value'])

# for i in len(df1):
#     want = pd.concat([want,pd.DataFrame])
    