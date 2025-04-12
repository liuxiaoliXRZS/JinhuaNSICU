import os
import pandas as pd
file_path = "./dataframe_uni_merge/转科历史.csv"
column_list = ["out_department",
"transfer_department",
"transfer_ward"
]


def extract_column_item(column_list):
    result_data = []
    try:
        df = pd.read_csv(file_path,encoding="gbk")
    except UnicodeDecodeError:
        df = pd.read_csv(file_path,encoding="utf-8")
    for column in column_list:
        # 提取某一列的不重复元素
        # column_values = df[column].unique()
        column_values = df[df[column] != ''][column].unique()

        # 将每一列的数据逐行添加到结果列表
        for value in column_values:
            result_data.append([column, value])

    # 创建包含结果数据的DataFrame
    result_df = pd.DataFrame(result_data, columns=['column_name', 'value_cn'])

    # 将DataFrame保存为CSV文件
    output_file_path = 'translation/转科历史_transfer.csv'
    result_df.to_csv(output_file_path, index=False)

extract_column_item(column_list)