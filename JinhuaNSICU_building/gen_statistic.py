import pandas as pd


input_file = "./dataframe_uni_merge_translated/Medical_record_front_page.csv"
output_file = "./temp/statistic.csv"

# 读取CSV文件
df = pd.read_csv(input_file)
# 将入院时间列解析为日期时间格式
df['admittime'] = pd.to_datetime(df['admittime'])
# 按入院时间升序排序
df = df.sort_values(by='admittime')
print(df)
df.to_csv(output_file,index=False)
# 删除重复ID的行
df_unique = df.drop_duplicates(subset="subject_id", keep="first")
# 根据病人ID筛选数据
selected_data = df_unique[['subject_id','patient_gender_en','age','dischtime_base','admission_route','discharge_type']]
selected_data['age'] = selected_data['age'].apply(lambda x:round(x/365,1))
selected_data['los_hospital_day'] = selected_data['dischtime_base'].apply(lambda x:round(x/(24*60),2))
selected_data = selected_data.drop('dischtime_base',axis = 1)
selected_data['death_hosp'] = selected_data['discharge_type'].apply(lambda x:1 if x =="死亡" else 0)
selected_data = selected_data.drop('discharge_type',axis = 1)
 # 将DataFrame保存到新的CSV文件
selected_data.to_csv(output_file, index=False)
