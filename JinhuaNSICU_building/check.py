import pandas as pd

# 读取第一个CSV文件
df1 = pd.read_csv(r'C:\Users\liuxiaoli\Desktop\神外_0714\患者.csv')

# 读取第二个CSV文件
df2 = pd.read_csv('dataframe_uni_merge_translated\病案首页.csv')

# 检查第一个CSV文件的subject_id列中的元素是否存在于第二个CSV文件的subject_id列中
df1['exists_in_file2'] = df1['patient_SN'].isin(df2['subject_id'])

# 筛选出存在的行
df_exists = df1[df1['exists_in_file2']]

# 删除辅助列
df_exists = df_exists.drop(columns=['exists_in_file2'])

# 将结果保存到新的CSV文件中
df_exists.to_csv('exists_in_file2.csv', index=False)

# 输出结果
print(df_exists)


# import pandas as pd

# # 加载CSV文件
# file_path = r'C:\Users\liuxiaoli\Desktop\神外_0714\生命体征.csv'
# # file_path = 'dataframe_uni_merge_translated\生命体征.csv'
# df = pd.read_csv(file_path)

# # 筛选出subject_id列等于特定值的行
# subject_id_value = '0e9d2b15b59a744f0c2f78f4148ecb8b'  # 替换为你要筛选的subject_id值
# filtered_df = df[df['patient_SN'] == subject_id_value]

# # 打印筛选后的数据
# print(filtered_df)

# import os
# import pandas as pd

# # 文件夹路径
# folder_path = r'C:\Users\liuxiaoli\Desktop\神外_0714'

# # 获取文件夹中的所有CSV文件
# csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

# # 遍历每个CSV文件，去除重复的行
# for file in csv_files:
#     file_path = os.path.join(folder_path, file)
    
#     # 读取CSV文件
#     df = pd.read_csv(file_path)
    
#     # 删除完全相同的行
#     df_unique = df.drop_duplicates()
    
#     # 保存去重后的数据到新的CSV文件中
#     new_file_path = os.path.join(r'C:\Users\liuxiaoli\Desktop\神外_0714\dataframe_uni', file)
#     df_unique.to_csv(new_file_path, index=False)
    
#     print(f"去除重复的行后的数据已保存到 {new_file_path}")

