import os
import pandas as pd

# 文件夹路径
folder_path = './dataframe_uni_merge'

# 获取文件夹中所有的CSV文件名
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

# 去除文件扩展名部分，只保留文件名
csv_file_names = [os.path.splitext(file)[0] for file in csv_files]

# 创建包含文件名的DataFrame
df = pd.DataFrame({'table_name_cn': csv_file_names})

# 将DataFrame保存为CSV文件
output_file_path = 'Table_transfer.csv'
df.to_csv(output_file_path, index=False)