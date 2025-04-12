import pandas as pd
import re

# df = pd.read_csv('0729v2\Drug_sensitivity.csv')

# # df['test_specimen_time_base'] = pd.to_numeric(df['test_specimen_time_base'],errors = 'coerce')
# df = df.groupby(['subject_id','hadm_id']).apply(lambda x:x.sort_values('test_time_base'))

# df = df.to_csv('0729v2\Drug_sensitivity.csv',index= False)

# df = pd.read_csv('0729v2\Examination.csv')


# # text = '两侧胸廓对称，气管居中。两肺纹理增多，两肺见片状密度增高影，边界模糊。心脏及大血管影位置、形态位于正常范围。两侧横膈光整，两侧肋膈角变钝。较前片2014-1-5进展。'
# def remove_dates(text):
#     text = re.sub('（临床操作医生：李颖如，卢斌）  联系电话：13429049868','',text)
#     return re.sub(r'\d{4}[-.]\d{1,2}[-.]\d{1,2}|\d{2}[-.]\d{2}', '****-**-**', text)

# df['examine_finding'] = df['examine_finding'].apply(lambda x: remove_dates(str(x)) if pd.notna(x) else x)
# df['inspection_conclusion'] = df['inspection_conclusion'].apply(lambda x: remove_dates(str(x)) if pd.notna(x) else x)
# # print(remove_dates(text))
# df.to_csv('0729v3/Examination.csv',index=False)

# df = pd.read_csv('0729v3\Examination.csv',encoding='gbk')
# from mtranslate import translate


# def translate_text(text):
#     try:
#         return translate(text,'en')
#     except Exception as e:
#         print(e)
#         return text
# df['check_name_en'] = df['check_name'].apply(lambda x:translate_text(str(x)) if pd.notna(x) else x)

# cols = df.columns.tolist()
# index = cols.index('check_name')
# cols.insert(index + 1,cols.pop(cols.index('check_name_en')))
# df = df[cols]

# df.to_csv('0729v3\Examination2.csv')

# df = pd.read_csv('0729v3\surgical_record_front_page.csv')
# # df = df.rename(columns={'prescription_starttime.1':'prescription_starttime_base'})
# df['surgery_endtime_base'] = pd.to_numeric(df['surgery_endtime_base'],errors = 'coerce')
# df = df.groupby(['subject_id','hadm_id']).apply(lambda x:x.sort_values('surgery_endtime_base'))

# df = df.to_csv('0729v2\surgical_record_front_page.csv',index= False)

import csv
import pandas as pd

def find_unique_elements(file1_path, col1_name, file2_path, col2_name):
    """找出在file1_path指定列名中存在但在file2_path指定列名中不存在的元素"""
    # 读取第一个CSV文件
    df1 = pd.read_csv(file1_path)
    
    # 读取第二个CSV文件
    df2 = pd.read_csv(file2_path)

    # 获取指定列的数据
    data1 = set(df1[col1_name])
    print(len(data1))
    data2 = set(df2[col2_name])
    print(len(data2))
    # print(data1 >= data2)
    # 计算差异
    unique_elements = data1.difference(data2)
    # unique_elements = data1.intersection(data2)
    return unique_elements

# 使用示例
file2_path = r'20240808_neurology\0809\生命体征2.csv'
# file2_path = 'dataframe_uni_merge_translated\Vital_signs.csv'
col1_name = 'hadm_id'  # 假设第一列的列名为'Column1'
file1_path = 'dataframe_uni_merge_translated\Vital_signs.csv'
col2_name = 'hadm_id'  # 假设第二列的列名为'Column1'

unique_elements = find_unique_elements(file1_path, col1_name, file2_path, col2_name)
df3 = pd.read_csv(r'20240808_neurology\0809\生命体征2(replace).csv')
df3 = df3[~((df3['hadm_id'].isin(unique_elements)) & (df3['subcategory_name_en'] == 'Respiratory'))]
df3.to_csv(r'20240808_neurology\0809\生命体征2(replaceAndDel).csv',index=False)
print(len(df3))
# data3 = set(df3['就诊标识（医渡云计算）'])
# eles = unique_elements.difference(data3)
# print("Elements unique to the first file:", unique_elements)
# print(len(unique_elements))


# def rename_column(file_path):
#     """读取CSV文件并重命名指定的列名，并保存结果到新文件"""
#     # 读取CSV文件
#     df = pd.read_csv(file_path, encoding='gbk')
    
#     # 重命名列
#     df = df.rename(columns={'patient_SN': 'subject_id',
#                             '就诊标识（医渡云计算）':'hadm_id',
#                             '生命体征子类名称':'subcategory_name',
#                             '生命体征查体值':'value',
#                             '生命体征子类单位':'subcategory_unit',
#                             '查体时间':'charttime'})
#     df = df.drop(columns = ['病案号','门诊号','住院号'],axis = 1)
#     # 保存到新文件
#     output_path = '20240808_neurology/0809/生命体征.csv'
#     df.to_csv(output_path, index=False, encoding='gbk')
    
#     return df

# # 使用示例
# file_path = '20240808_neurology/0809/生命体征.csv'


# # 读取文件、重命名列并保存到新文件
# df_renamed = rename_column(file_path)

# # 显示修改后的DataFrame
# print(df_renamed.head())