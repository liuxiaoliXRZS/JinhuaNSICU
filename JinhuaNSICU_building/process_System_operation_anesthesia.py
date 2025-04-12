import pandas as pd

df = pd.read_csv('0729v3\System_operation_anesthesia(split).csv')




# 创建一个空的DataFrame来存储拆分后的数据
expanded_rows = []

# 遍历每一行，拆分药品信息和时间戳，并将其展开
for index, row in df.iterrows():
    # print(row)
    input_type_list = row['input_type'].split(';') if pd.notna(row['input_type']) else []
    drug_info_list = row['intraoperative_medication'].split(';') if pd.notna(row['intraoperative_medication']) else []
    timestamp_list = row['medication_starttime_base'].split(';') if pd.notna(row['medication_starttime_base']) else []
    # print(drug_info_list)
    # print(timestamp_list)
    # 确保药品信息和时间戳数量相同
    if len(drug_info_list) == len(timestamp_list):
        for input_type, drug, timestamp in zip(input_type_list,drug_info_list, timestamp_list):
            expanded_row = row.to_dict()
            expanded_row['input_type'] = input_type
            expanded_row['intraoperative_medication'] = drug
            expanded_row['medication_starttime_base'] = timestamp
            expanded_rows.append(expanded_row)
    else:
        print(input_type_list)
        print(drug_info_list)
        print(timestamp_list)
        print(f"行 {index} 的药品信息和时间戳数量不匹配，已跳过。")
# 将拆分后的数据转换为DataFrame
expanded_df = pd.DataFrame(expanded_rows)

# 将结果保存到新的CSV文件
output_file_path = '0729v3/System_operation_anesthesia(split).csv'  # 你想要保存的新文件路径
expanded_df.to_csv(output_file_path, index=False)

# print(f"已成功拆分药品信息和时间戳，并将结果保存到 {output_file_path}")

# df['medication_starttime_base'] = pd.to_numeric(df['medication_starttime_base'],errors = 'coerce')
# df = df.groupby(['subject_id','hadm_id']).apply(lambda x:x.sort_values('medication_starttime_base'))
# df.to_csv('0729v3\System_operation_anesthesia(split).csv',index=False)  
# column_name = 'intraoperative_medication'
# unique = df[column_name].unique()
# unique_df = pd.DataFrame(unique,columns=[column_name])
# unique_df.to_excel('trans_columns'+'\E_'+column_name+'.xlsx' ,index=False)