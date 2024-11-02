import pandas as pd
df = pd.read_csv('0802v1/orders.csv')

admit_record = df[(df['order_content'] == '病人住院')| (df['order_content'] == '重症病人住院')]
print(len(admit_record))

# 对于每个subject_id，保留admittime最小的那一行
admit_record = admit_record.groupby('subject_id').apply(lambda x: x.nsmallest(1, 'starttime_base')).reset_index(drop=True)

# 保存结果到新的CSV文件
admit_record.to_csv('入院时间调整.csv', index=False)