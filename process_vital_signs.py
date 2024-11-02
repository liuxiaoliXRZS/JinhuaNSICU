import pandas as pd

# df = pd.read_csv('神外_0714\dataframe_uni\生命体征.csv',encoding='gbk')




# # 创建一个空的DataFrame来存储拆分后的数据
# expanded_rows = []

# # 遍历每一行，拆分药品信息和时间戳，并将其展开
# for index, row in df.iterrows():
#     # print(row)
#     name_list = [item for item in row['生命体征子类名称'].split(';') if item] if pd.notna(row['生命体征子类名称']) else []
#     number_list = [item for item in row['生命体征查体值'].split(';') if item] if pd.notna(row['生命体征查体值']) else []
#     unit_list = [item for item in row['生命体征子类单位'].split(';') if item] if pd.notna(row['生命体征子类单位']) else []
#     timestamp_list = [item for item in row['查体时间'].split(';') if item] if pd.notna(row['查体时间']) else []
#     # print(drug_info_list)
#     # print(timestamp_list)
#     # 确保药品信息和时间戳数量相同
#     if len(number_list) == len(timestamp_list):
#         for name, number, unit, timestamp in zip(name_list,number_list, unit_list,timestamp_list):
#             expanded_row = row.to_dict()
#             expanded_row['生命体征子类名称'] = name
#             expanded_row['生命体征查体值'] = number
#             expanded_row['生命体征子类单位'] = unit
#             expanded_row['查体时间'] = timestamp
#             expanded_rows.append(expanded_row)
#     else:
#         print(len(name_list))
#         print(len(number_list))
#         print(len(unit_list))
#         print(len(timestamp_list))
#         print(f"行 {index} 的药品信息和时间戳数量不匹配，已跳过。")
#         # break

# # 将拆分后的数据转换为DataFrame
# expanded_df = pd.DataFrame(expanded_rows)

# # 将结果保存到新的CSV文件
# output_file_path = '神外_0714\dataframe_uni\生命体征(split).csv'  # 你想要保存的新文件路径
# expanded_df.to_csv(output_file_path, index=False)

# print(f"已成功拆分药品信息和时间戳，并将结果保存到 {output_file_path}")

# df['medication_starttime_base'] = pd.to_numeric(df['medication_starttime_base'],errors = 'coerce')
# df = df.groupby(['subject_id','hadm_id']).apply(lambda x:x.sort_values('medication_starttime_base'))
# df.to_csv('0729v3\System_operation_anesthesia(split).csv',index=False)  
# column_name = 'intraoperative_medication'
# unique = df[column_name].unique()
# unique_df = pd.DataFrame(unique,columns=[column_name])
# unique_df.to_excel('trans_columns'+'\E_'+column_name+'.xlsx' ,index=False)


# 读取旧的和新的CSV文件
old_df = pd.read_csv('0729v1/Vital_signs.csv')
new_df = pd.read_csv('20240808_neurology/0809/生命体征2.csv')

# 筛选出新的文件中只有呼吸数据的行
new_respiration_df = new_df[new_df['subcategory_name_en'] == 'Respiratory']

# 通过merge操作，将新的呼吸数据合并到旧数据中
updated_df = old_df.merge(new_respiration_df[['hadm_id', 'subcategory_name_en','charttime_base','value']], 
                          on=['hadm_id', 'subcategory_name_en','charttime_base'], 
                          how='left', 
                          suffixes=('', '_new'))

# 更新旧数据的呼吸列，只有当type_column为'respiration'时才替换
updated_df['value'] = updated_df['value_new'].combine_first(updated_df['value'])

# 删除临时列
updated_df.drop(columns=['value_new'], inplace=True)

# 保存更新后的DataFrame到新的CSV文件
updated_df.to_csv('20240808_neurology/0809/生命体征2(replace).csv', index=False)
