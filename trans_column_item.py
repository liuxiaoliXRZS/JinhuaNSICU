import pandas as pd

# 读取Excel文件中的键值对
def read_mapping_from_excel(excel_file, key_column, value_column):
    df = pd.read_csv(excel_file,encoding='gbk')
    df = df.drop_duplicates(keep='first')
    return dict(zip(df[key_column], df[value_column]))

# 应用映射到CSV文件的某一列
def apply_mapping_to_csv(input_csv_file, output_csv_file, column_to_map, mapping_dict,add_column):
    df = pd.read_csv(input_csv_file)
    # df = df.drop(columns=['order_department_en','executive_department_en'],inplace = False)
    # 应用映射，处理NaN值
    if column_to_map in df.columns:
        if add_column:
            column_to_map_en = column_to_map +'_en'
            df[column_to_map_en] = df[column_to_map].map(mapping_dict).fillna(df[column_to_map])
        else:
            df[column_to_map] = df[column_to_map].map(mapping_dict).fillna(df[column_to_map])
    else:
        print(f"Column '{column_to_map}' not found in the CSV file.")
    if add_column:
        cols = df.columns.tolist()
        index = cols.index(column_to_map)
        cols.insert(index + 1,cols.pop(cols.index(column_to_map_en)))
        df = df[cols]

    # 保存处理后的数据到新的CSV文件
    df.to_csv(output_csv_file, index=False)
    print(f"Processed CSV has been saved to {output_csv_file}")

# 输入文件路径
keyword = 'chief_complaint'
excel_file = 'trans_columns\E_' + keyword +'.csv'
excel_file = 'department_unique.csv'
input_csv_file = '0903v1/transfer.csv'
output_csv_file = '0903v1/transfer.csv'
key_column = 'department_cn' # 替换为Excel文件中包含键的列名
value_column = 'department_en'   # 替换为Excel文件中包含值的列名
column_to_map = 'transfer_department'  # 替换为需要映射的CSV列名

# 读取映射字典
mapping_dict = read_mapping_from_excel(excel_file, key_column, value_column)

# 应用映射到CSV文件
apply_mapping_to_csv(input_csv_file, output_csv_file, column_to_map, mapping_dict,True)