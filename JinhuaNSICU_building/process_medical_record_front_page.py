import pandas as pd

# df = pd.read_csv('0802v1/Medical_record_front_page.csv')

# df['age'] = df['age'].apply(lambda x: int(x/365) if pd.notna(x) else x)
# df.to_csv('0802v1/Medical_record_front_page.csv',index=False)
# unique = df['discharge_ward'].unique()
# unique_df = pd.DataFrame(unique,columns=['discharge_ward'])
# unique_df.to_excel('discharge_ward.xlsx',index=False)

# 读取Excel文件中的键值对
def read_mapping_from_excel(excel_file, key_column, value_column):
    df = pd.read_csv(excel_file,encoding='gbk')
    df = df.drop_duplicates(keep='first')
    return dict(zip(df[key_column], df[value_column]))

# 应用映射到CSV文件的某一列
def apply_mapping_to_csv(input_csv_file, output_csv_file, column_to_map, mapping_dict):
    df = pd.read_csv(input_csv_file)
    
    # 应用映射，处理NaN值
    if column_to_map in df.columns:
        df[column_to_map] = df[column_to_map].map(mapping_dict).fillna(df[column_to_map])
    else:
        print(f"Column '{column_to_map}' not found in the CSV file.")
    # df['age'] = df['age'].apply(lambda x: int(x/365) if pd.notna(x) else x)
    # 保存处理后的数据到新的CSV文件
    df.to_csv(output_csv_file, index=False)
    print(f"Processed CSV has been saved to {output_csv_file}")

# 输入文件路径
excel_file = 'department_unique.csv'
input_csv_file = '0903v1/transfer.csv'
output_csv_file = '0903v1/transfer.csv'
key_column = 'department_unique'  # 替换为Excel文件中包含键的列名
value_column = 'department_cn'  # 替换为Excel文件中包含值的列名
column_to_map = 'transfer_department'  # 替换为需要映射的CSV列名

# 读取映射字典
# mapping_dict = read_mapping_from_excel(excel_file, key_column, value_column)

# # 应用映射到CSV文件
# apply_mapping_to_csv(input_csv_file, output_csv_file, column_to_map, mapping_dict)

# # 1. 计算每个患者的入院次数
# admission_counts = df.groupby('subject_id')['hadm_id'].nunique()

# # 2. 统计多次入院的患者数量和总患者数量
# multiple_admissions = admission_counts[admission_counts > 1].count()
# total_patients = admission_counts.count()
# print('总的入院次数：',total_patients)
# # 3. 计算比例
# proportion = multiple_admissions / total_patients

# print(f'多次入院患者的比例是：{proportion:.2%}')

# df['admittime'] = pd.to_datetime(df['admittime'],format = '%Y%m%d %H:%M:%S')

# # 2. 筛选多次入院患者
# multiple_admission_ids = admission_counts[admission_counts > 1].index
# multiple_admissions = df[df['subject_id'].isin(multiple_admission_ids)]

# # 3. 计算每个患者的时间跨度
# grouped = multiple_admissions.groupby('subject_id')['admittime']
# first_admission = grouped.min()
# last_admission = grouped.max()
# time_spans = (last_admission - first_admission).dt.total_seconds() / (365.25 * 24 * 3600)

# # 4. 计算中位数和四分位数
# median_span = time_spans.median()
# q1_span = time_spans.quantile(0.25)
# q3_span = time_spans.quantile(0.75)

# print(f'时间跨度的中位数是：{median_span:.2f} 年')
# print(f'第一四分位数（Q1）：{q1_span:.2f} 年')
# print(f'第三四分位数（Q3）：{q3_span:.2f} 年')

# multiple_admission_counts = admission_counts[admission_counts > 1]

# # 3. 计算中位数和四分位数
# median_admissions = multiple_admission_counts.median()
# q1_admissions = multiple_admission_counts.quantile(0.25)
# q3_admissions = multiple_admission_counts.quantile(0.75)

# print(f'多次入院患者入院次数的中位数是：{median_admissions}')
# print(f'第一四分位数（Q1）：{q1_admissions}')
# print(f'第三四分位数（Q3）：{q3_admissions}')


def add_admission_columns(home_page_csv, admission_time_csv, output_csv):
    home_page_df = pd.read_csv(home_page_csv, encoding='gbk')
    admission_time_df = pd.read_csv(admission_time_csv,encoding='gbk')

    # 将admission_time_df的subject_id列转换为字符串类型
    admission_time_df['year'] = pd.to_datetime(admission_time_df['admittime'],format = '%Y%m%d %H:%M').dt.year
    admission_time_df['admittime'] = pd.to_datetime(admission_time_df['admittime'],format = '%Y%m%d %H:%M')
    # 按照入院时间排序，并给每个subject_id分配顺序
    admission_time_df['admitted_rank'] = admission_time_df.groupby('subject_id')['admittime'].rank(method='first',ascending=True).astype(int)
    print(admission_time_df)
    # 将提取的年份和顺序合并到病案首页表中
    merged_df = pd.merge(home_page_df, admission_time_df[['subject_id', 'hadm_id','year', 'admitted_rank']], on=['subject_id','hadm_id'], how='left')
    print(merged_df)
    # 保存新的CSV文件
    merged_df.to_csv(output_csv, index=False)

    print(f"结果已保存到 {output_csv}")
add_admission_columns('0903v1/medical_record_front_page.csv','0802v1/medical_record_front_page.csv','0903v1/medical_record_front_page(add).csv')