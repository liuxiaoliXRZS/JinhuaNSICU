import pandas as pd

df = pd.read_csv('0729v2\operation.csv')

# df['starttime_base'] = pd.to_numeric(df['starttime_base'],errors = 'coerce')
# df = df.groupby(['subject_id','hadm_id']).apply(lambda x:x.sort_values('starttime_base'))

# df = df.to_csv('0729v2\operation.csv',index= False)


import re
# df = pd.read_csv('0729v3\Medical_record.csv')


# text = '两侧胸廓对称，气管居中。两肺纹理增多，两肺见片状密度增高影，边界模糊。心脏及大血管影位置、形态位于正常范围。两侧横膈光整，两侧肋膈角变钝。较前片2014-1-5进展。'
def remove_dates(text):
    # text = re.sub('（临床操作医生：李颖如，卢斌）  联系电话：13429049868','',text)
    return re.sub(r'\d{4}[-.]\d{1,2}[-.]\d{1,2}|\d{2}[-.]\d{2}|\d{8}', '****-**-**', text)

df['procedure_description'] = df['procedure_description'].apply(lambda x: remove_dates(str(x)) if pd.notna(x) else x)

# print(remove_dates(text))
df.to_csv('0729v3/operation(rm_privacy).csv',index=False)