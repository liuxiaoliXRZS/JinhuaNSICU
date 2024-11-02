import re
import pandas as pd

df = pd.read_csv('0903v1/Examination.csv',encoding='gbk')

def remove_dates(text):
    # text = re.sub('（临床操作医生：李颖如，卢斌）  联系电话：13429049868','',text)
    return re.sub(r'\d{4}[-.]\d{1,2}[-.]\d{1,2}|\d{2}[-.]\d{2}|\d{8}', '****-**-**', text)

# 定义函数删除 8 位数字
def remove_eight_digit_numbers(text):
    return re.sub(r'\b\d{8}\b', '', str(text)).strip()

df['check_part'] = df['check_part'].apply(lambda x: remove_eight_digit_numbers(str(x)) if pd.notna(x) else x)
df['check_part_en'] = df['check_part_en'].apply(lambda x: remove_eight_digit_numbers(str(x)) if pd.notna(x) else x)

df.to_csv('0903v1/Examination.csv',index = False)