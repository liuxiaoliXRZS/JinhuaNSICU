import csv
import os
import pandas as pd

folder_path = "20240808_neurology"  # 替换为您的文件夹路径
base_filename = "生命体征."  # 替换为您的基本文件名

merged_data = []  # 用于存储合并后的数据
header_added = False  # 标记是否已添加标题行

# 遍历文件夹中的所有文件
for file_name in os.listdir(folder_path):
    if file_name.startswith(base_filename) and file_name.endswith(".csv"):
        file_path = os.path.join(folder_path, file_name)
        print(file_path)
        # 访问每一行的内容
        with open(file_path, "r",encoding='gbk') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            # 读取 CSV 文件的内容
            for row in csv_reader:
                if not header_added:
                    merged_data.append(row.keys())  # 添加标题行
                    # print(row.keys())
                    header_added = True
                merged_data.append(row.values())  # 添加数据行
                # print(row.values())

# 将合并后的数据写入新的 CSV 文件
output_file_path = os.path.join("20240808_neurology/0809/", base_filename + "csv")
with open(output_file_path, "w", newline="") as output_file:
    csv_writer = csv.writer(output_file)
    csv_writer.writerows(merged_data)

print(f"合并后的数据已保存到文件: {output_file_path}")


# import os
# import pandas as pd

# # 定义两个文件夹的路径
# folder_path_1 = r"C:\Users\liuxiaoli\Desktop\神外_0714\part1_20240710-1617"  # 替换为第一个文件夹的路径
# folder_path_2 = r"C:\Users\liuxiaoli\Desktop\神外_0714\part2_20240710-1436"  # 替换为第二个文件夹的路径

# # 获取两个文件夹中的文件名
# files_1 = set(os.listdir(folder_path_1))
# files_2 = set(os.listdir(folder_path_2))

# # 找出两个文件夹中都存在的CSV文件
# common_files = files_1.intersection(files_2)
# common_csv_files = [file for file in common_files if file.endswith('.csv')]

# # 定义输出文件夹
# output_directory = r"C:\Users\liuxiaoli\Desktop\神外_0714"
# if not os.path.exists(output_directory):
#     os.makedirs(output_directory)

# # 遍历所有相同的CSV文件
# for file_name in common_csv_files:
#     file_path_1 = os.path.join(folder_path_1, file_name)
#     file_path_2 = os.path.join(folder_path_2, file_name)
    
#     # 读取两个文件到两个DataFrame中
#     df1 = pd.read_csv(file_path_1, encoding='gbk')
#     df2 = pd.read_csv(file_path_2, encoding='gbk')
    
#     # 按行合并两个DataFrame
#     combined_df = pd.concat([df1, df2], axis=0, ignore_index=True)
    
#     # 保存合并后的DataFrame到新的CSV文件，文件名与原文件名相同
#     output_file_path = os.path.join(output_directory, file_name)
#     combined_df.to_csv(output_file_path, index=False)

#     print(f"合并后的数据已保存到文件: {output_file_path}")

