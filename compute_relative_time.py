import pandas as pd

# 读取CSV文件
admissions_df = pd.read_csv('dataframe_uni_merge_translated/病案首页.csv', parse_dates=['admittime'])
vitals_df = pd.read_csv('20240808_neurology/0809/生命体征1.csv', parse_dates=['charttime'])

# 确保日期列被正确解析为datetime类型
admissions_df['admittime'] = pd.to_datetime(admissions_df['admittime'],format = '%Y%m%d %H:%M:%S')
vitals_df['charttime'] = pd.to_datetime(vitals_df['charttime'],format = '%Y%m%d %H:%M:%S')

# 合并两个数据集
merged_df = pd.merge(vitals_df, admissions_df[['hadm_id', 'admittime']], on='hadm_id')

# 计算时间差
merged_df['charttime_base'] = (merged_df['charttime'] - merged_df['admittime']).dt.total_seconds() / 60
merged_df['charttime_base'] = merged_df['charttime_base'].round().astype(int)
# 删除不需要的列
merged_df.drop(columns=['admittime'], inplace=True)

# 保存更新后的生命体征CSV文件
merged_df.to_csv('20240808_neurology/0809/生命体征2.csv', index=False)

# 查看处理后的数据
print(merged_df.head())