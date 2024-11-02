# from translate import Translator
import os
import pandas as pd

folder_path = "./translation_adden"


for filename in os.listdir(folder_path):
    if filename.endswith("_transfer.csv"):
        file_path = os.path.join(folder_path, filename)
        print(file_path)

        # 查找"_transfer"的位置
        index = filename.find("_transfer")
        if index != -1:
            trans_filename = filename[:index] + filename[index + len("_transfer"):]
        else:
            trans_filename = filename

        try:
            df = pd.read_csv(file_path,encoding="gbk")
        except UnicodeDecodeError:
            df = pd.read_csv(file_path,encoding="utf-8")
        column_name = list(df["column_name"].unique())
        eng_list = list(df["value_en"])
        chi_list = list(df["value_cn"])

        name_dic={}
        for idx in range(len(eng_list)):
            if str(chi_list[idx])!="nan" and chi_list[idx] not in name_dic:
                name_dic[chi_list[idx]]=eng_list[idx]
        try:
            df_trans = pd.read_csv("./dataframe_uni_merge/"+trans_filename, encoding="utf-8")
        except UnicodeDecodeError:
            df_trans = pd.read_csv("./dataframe_uni_merge/"+trans_filename, encoding="gbk")
        cur_list = []
        # 遍历要翻译的列
        for column in column_name:
            df_trans["temp"] = df_trans[column].map(name_dic).fillna(df_trans[column])

            # 将已翻译列插入到翻译列后面
            column_index = df_trans.columns.get_loc(column)
            df_trans.insert(column_index + 1, column+"_en", df_trans["temp"])

            df_trans.drop("temp",axis = 1,inplace= True)
        # 修改后的表有时候会出现“Unnamed”的列，我们要把它去掉    
        cur_col_list = df_trans.columns.tolist()
        for cur_col in cur_col_list:
            if 'Unnamed' in cur_col:
                cur_list.append("")
            else:
                cur_list.append(cur_col)
        # 创建字典，将新的列名与旧的列名对应起来
        rename_dict = {old_name: new_name for old_name, new_name in zip(cur_col_list, cur_list)}
        # 使用rename()方法替换列名
        df_trans = df_trans.rename(columns=rename_dict)
        df_trans.to_csv("./translated/"+trans_filename,index = False)
   

