import matplotlib.pyplot as plt
import pandas as pd
import datetime

# 示例数据
data = {
    'Procedure': ['Appendectomy', 'Cholecystectomy', 'Hernia Repair'],  #手术名称
    'Start Time': ['2024-06-01 08:00', '2024-06-02 09:30', '2024-06-03 11:00'], # 
    'End Time': ['2024-06-01 10:00', '2024-06-02 12:00', '2024-06-03 13:00'],
    'Anesthesia': ['General', 'Local', 'General']   # 麻醉
}

# 转换为DataFrame
df = pd.DataFrame(data)
df['Start Time'] = pd.to_datetime(df['Start Time'])
df['End Time'] = pd.to_datetime(df['End Time'])

# 计算持续时间
df['Duration'] = df['End Time'] - df['Start Time']

# 创建甘特图
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制每个手术的条状图
for i, row in df.iterrows():
    ax.barh(row['Procedure'], row['Duration'].total_seconds() / 3600, left=row['Start Time'], height=0.4, label=row['Anesthesia'])

# 设置标签和标题
ax.set_xlabel('Time')
ax.set_ylabel('Procedure')
ax.set_title('Hospital Surgery Schedule')
plt.legend(title='Anesthesia Type')

# 显示图形
plt.show()
