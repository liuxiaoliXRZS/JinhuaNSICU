import os
import pandas as pd
def find_repeat_name(col_list):
    result = []
    for item in col_list:
        if isinstance(item, str) and item.endswith(".1"):
            result.append(item[:-2])
    return result

def rename_duplicate_columns(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            cur_list = []
            file_path = os.path.join(folder_path, filename)
            print(file_path)
            df = pd.read_csv(file_path,encoding="gbk")
            cur_col_list = df.columns.tolist()
            print(cur_col_list)
            for cur_col in cur_col_list:
                if 'Unnamed' in cur_col:
                    cur_list.append("")
                elif ".1" in cur_col:
                    cur_list.append(str(cur_col[:-2]+"_base"))
                else:
                    cur_list.append(cur_col)
            print(cur_list)
            # 创建字典，将新的列名与旧的列名对应起来
            rename_dict = {old_name: new_name for old_name, new_name in zip(cur_col_list, cur_list)}
            # 使用rename()方法替换列名
            df = df.rename(columns=rename_dict)
            output_file = "dataframe_uni/" + filename 
            df.to_csv(output_file, index=False)
# 指定文件夹路径
folder_path = "./dataframe"

# 调用函数进行重命名
rename_duplicate_columns(folder_path)
