import pandas as pd

# 读取CSV文件
df1 = pd.read_csv('0802v1/Surgical_record_front_page.csv')

# 先填充 NaN 为空字符串，然后进行筛选
filtered_df1 = df1[df1['surgery_name_norm'].fillna('').apply(lambda x: not (
    '静脉穿刺' in x or '气管插管' in x or '气管切开' in x or '腰椎穿刺' in x or '支气管镜检查' in x))]

print(len(filtered_df1))
filtered_df1.to_csv('0802v1/Surgical_record_front_page(remove).csv', index=False)