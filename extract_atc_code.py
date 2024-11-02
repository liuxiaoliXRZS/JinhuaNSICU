import re
import pandas as pd
def extract_atc_code():
    file_path = "./dataframe_uni_merge/用药.csv"

    try:
        df = pd.read_csv(file_path,encoding="gbk")
    except UnicodeDecodeError:
        df = pd.read_csv(file_path,encoding="utf-8")
    df = df.dropna(subset=["atc_code"])

    atc_code = df["atc_code"].unique()
    dict = {}
    for sentence in atc_code:
        if sentence == '' or not sentence:
            continue
        else:
            pattern = r"([A-Za-z0-9]+)(([^)]+))"

            matches = re.findall(pattern,sentence)
            for match in matches:
                name = match[0]
                print(name)
                discription = match[1].lstrip("(")
                print(discription)
                if name not in dict:
                    dict[name] = discription
    code = []
    content = []
    print(dict)
    for key,value in dict.items():
        code.append(key)
        content.append(value)
    df_new = pd.DataFrame({"code":code,"content":content})

    df_new.to_csv("./atc_code.csv",index = False)


def del_atc_code_bracket_content():
    file_path = "./dataframe_uni_merge_translated/Medication.csv"

    try:
        df = pd.read_csv(file_path,encoding="gbk")
    except UnicodeDecodeError:
        df = pd.read_csv(file_path,encoding="utf-8")
    new_atc_code = []
    atc_code = df["atc_code"]
    for sentence in atc_code:
        if str(sentence) == 'nan':
            new_atc_code.append('')
        else:
            cleaned_text = re.sub(r'\([^)]*\)', '', sentence)
            new_atc_code.append(cleaned_text)

    df["atc_code"] = new_atc_code
    df = df.drop("atc_code_en",axis = 1)
    df.to_csv("./Medication.csv",index = False)

del_atc_code_bracket_content()