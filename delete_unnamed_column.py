import pandas as pd
import os
# 如果表头出现了Unnamed字样，请使用此函数
def delete_unnamed_column(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(folder_path, filename)
            print(file_path)
        try:
            df = pd.read_csv(file_path,encoding="gbk")
        except UnicodeDecodeError:
            df = pd.read_csv(file_path,encoding="utf-8")
        cur_list = []
        # 修改后的表有时候会出现“Unnamed”的列，我们要把它去掉    
        cur_col_list = df.columns.tolist()
        for cur_col in cur_col_list:
            if 'Unnamed' in cur_col:
                cur_list.append("")
            else:
                cur_list.append(cur_col)
        # 创建字典，将新的列名与旧的列名对应起来
        rename_dict = {old_name: new_name for old_name, new_name in zip(cur_col_list, cur_list)}
        # 使用rename()方法替换列名
        df = df.rename(columns=rename_dict)
        df.to_csv(folder_path+"/"+filename,index = False)

delete_unnamed_column("0903v1")
     

