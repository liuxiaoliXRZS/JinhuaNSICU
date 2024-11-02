# from translate import Translator
import os
import pandas as pd

folder_path = "./translation_adden"

for filename in os.listdir(folder_path):
    if filename.endswith("_transfer.csv"):
        file_path = os.path.join(folder_path, filename)
        print(file_path)
        try:
            df = pd.read_csv(file_path,encoding="gbk")
        except UnicodeDecodeError:
            df = pd.read_csv(file_path,encoding="utf-8")

        # 创建Translator对象
        # translator = Translator(to_lang = "en")
    
        # 翻译"value_cn"列的值并存储到"value_en"列
        df["value_en"] = df["value_en"].apply(lambda x:x[0].upper()+x[1:] if x and type(x) == str and x[0].isalpha() else x)

        df.to_csv("./translation_readd/"+filename,index = False)
