# from translate import Translator
import os
import pandas as pd

folder_path = "./dataframe_uni_merge_translated"
df = pd.read_csv("./Table_transfer.csv",encoding="gbk")

eng_list = list(df["table_name_en"])
chi_list = list(df["table_name_cn"])

name_dic={}
for idx in range(len(eng_list)):
    if str(chi_list[idx])!="nan" and chi_list[idx] not in name_dic:
        name_dic[chi_list[idx]]=eng_list[idx]

for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        file_path = os.path.join(folder_path, filename)
        print(file_path)
        try:
            df = pd.read_csv(file_path,encoding="gbk")
        except UnicodeDecodeError:
            df = pd.read_csv(file_path,encoding="utf-8")
        # 翻译文件名（不包括后缀名）
        file_name = os.path.splitext(filename)[0]
        translated_file_name = name_dic.get(file_name, file_name)

        # 构建输出文件路径
        output_file = os.path.join(folder_path, translated_file_name + ".csv")

        # 保存到输出CSV文件
        df.to_csv(output_file, index=False)

