import pandas as pd

# df = pd.read_csv('0729v2\Transfer.csv')

# column_name = 'out_ward'
# unique = df[column_name].unique()
# unique_df = pd.DataFrame(unique,columns=[column_name])
# unique_df.to_excel(column_name+'.xlsx' ,index=False)
df = pd.read_csv('0729v3\Transfer.csv')

df['outtime_base'] = pd.to_numeric(df['outtime_base'],errors = 'coerce')
df = df.groupby(['subject_id','hadm_id']).apply(lambda x:x.sort_values('outtime_base'))

df = df.to_csv('0729v3\Transfer.csv',index= False)


# def read_mapping_from_excel(excel_file, key_column, value_column):
#     df = pd.read_excel(excel_file)
#     df = df.drop_duplicates(keep='first')
#     return dict(zip(df[key_column], df[value_column]))

# # 应用映射到CSV文件的某一列
# def apply_mapping_to_csv(input_csv_file, output_csv_file, column_to_map, mapping_dict):
#     df = pd.read_csv(input_csv_file)
    
#     # 应用映射，处理NaN值
#     if column_to_map in df.columns:
#         df[column_to_map] = df[column_to_map].map(mapping_dict).fillna(df[column_to_map])
#     else:
#         print(f"Column '{column_to_map}' not found in the CSV file.")
#     # df['age'] = df['age'].apply(lambda x: int(x/365) if pd.notna(x) else x)
#     # 保存处理后的数据到新的CSV文件
#     df.to_csv(output_csv_file, index=False)
#     print(f"Processed CSV has been saved to {output_csv_file}")

# # 输入文件路径
# excel_file = 'discharge_ward.xlsx'
# input_csv_file = '0729v3\Transfer.csv'
# output_csv_file = '0729v3\Transfer.csv'
# key_column = 'discharge_ward'  # 替换为Excel文件中包含键的列名
# value_column = 'projection'  # 替换为Excel文件中包含值的列名
# column_to_map = 'transfer_department'  # 替换为需要映射的CSV列名

# # 读取映射字典
# mapping_dict = read_mapping_from_excel(excel_file, key_column, value_column)

# # 应用映射到CSV文件
# apply_mapping_to_csv(input_csv_file, output_csv_file, column_to_map, mapping_dict)