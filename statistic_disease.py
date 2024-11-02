import pandas as pd
import re
def count_column_values(csv_file,column_name,output_file):
    df = pd.read_csv(csv_file)
    df = df[(df['diagnosis_type'] == '入院诊断')]
    # df = df[df['diagnosis_type'] == '出院诊断']
    value_counts = df[column_name].value_counts()

    result_df = pd.DataFrame({column_name:value_counts.index,'count':value_counts.values})

    result_df.to_csv(output_file,index = False)

# count_column_values(r"C:\Users\liuxiaoli\Documents\WeChat Files\wxid_mhdypvby9ogw32\FileStorage\File\2024-08\mimic_ns_diagnosis.csv",'diagnosis_name_original','./statistic/admission_diagnosis2.csv')

def admission_disease_type():

    def remove_repeated_element(string):
        # 使用 split() 方法将字符串拆分成列表
        elements = string.split(';')

        # 使用集合（Set）去除重复元素
        unique_elements = set(elements)

        # 将去重后的元素转换回字符串，使用分号进行连接
        result = ';'.join(unique_elements)

        return result
    
    # 读取原始CSV文件
    df = pd.read_csv('./dataframe_uni_merge_translated/诊断.csv')

    # 根据subject_id、hadm_id和入院诊断这三列，合并icd_10列
    grouped = df.groupby(['subject_id', 'hadm_id', 'diagnosis_type'])['icd10_code'].apply(lambda x: ';'.join(x.fillna('').astype(str))).reset_index()
  
    grouped['icd10_code'] = grouped['icd10_code'].apply(remove_repeated_element)
    # 保存到新的CSV文件
    grouped.to_csv('uni_admission_disease.csv', index=False)

    df = pd.read_csv('./uni_admission_disease.csv')

    filtered_df = df[(df['diagnosis_type'] == '入院诊断')|(df['diagnosis_type'] == '转入诊断')]
    print(len(filtered_df))
    # 定义正则表达式模式
    pattern = r'[A-Za-z0-9./]+'

    # 提取数据并存放在一个新的列表中
    extracted_data = []
    for index, row in filtered_df.iterrows():
        data = str(row['icd10_code'])  # 替换为您的列名
        extracted_data.extend(re.findall(pattern, data))

    # 将提取的数据保存到新的CSV文件中
    df_extracted = pd.DataFrame(extracted_data, columns=['icd10_code'])
    # df_extracted.to_csv('your_output_file.csv', index=False)


    value_counts = df_extracted['icd10_code'].value_counts()

    result_df = pd.DataFrame({'admission_diagnosis':value_counts.index,'count':value_counts.values})

    result_df.to_csv('./statistic/admission_diagnosis.csv',index = False)

# admission_disease_type()

def discharge_disease_type():

    def remove_repeated_element(string):
        # 使用 split() 方法将字符串拆分成列表
        elements = string.split(';')

        # 使用集合（Set）去除重复元素
        unique_elements = set(elements)

        # 将去重后的元素转换回字符串，使用分号进行连接
        result = ';'.join(unique_elements)

        return result
    
    # 读取原始CSV文件
    df = pd.read_csv('./dataframe_uni_merge_translated/诊断.csv')

    # 根据subject_id、hadm_id和入院诊断这三列，合并icd_10列
    grouped = df.groupby(['subject_id', 'hadm_id', 'diagnosis_type'])['icd10_code'].apply(lambda x: ';'.join(x.fillna('').astype(str))).reset_index()
  
    grouped['icd10_code'] = grouped['icd10_code'].apply(remove_repeated_element)
    # 保存到新的CSV文件
    grouped.to_csv('uni_admission_disease.csv', index=False)

    df = pd.read_csv('./uni_admission_disease.csv')

    filtered_df = df[df['diagnosis_type'] == '出院诊断']
    print(len(filtered_df))
    # 定义正则表达式模式
    pattern = r'[A-Za-z0-9./]+'

    # 提取数据并存放在一个新的列表中
    extracted_data = []
    for index, row in filtered_df.iterrows():
        data = str(row['icd10_code'])  # 替换为您的列名
        extracted_data.extend(re.findall(pattern, data))

    # 将提取的数据保存到新的CSV文件中
    df_extracted = pd.DataFrame(extracted_data, columns=['icd10_code'])
    # df_extracted.to_csv('your_output_file.csv', index=False)


    value_counts = df_extracted['icd10_code'].value_counts()

    result_df = pd.DataFrame({'discharge_diagnosis':value_counts.index,'count':value_counts.values})

    result_df.to_csv('./statistic/discharge_diagnosis.csv',index = False)

# discharge_disease_type()

# import pandas as pd

# 读取CSV文件
df1 = pd.read_csv('statistic/discharge_diagnosis2.csv')
df2 = pd.read_csv('statistic/admission_diagnosis2.csv')
contain_content = '脑梗死'
not_contain_content = '创伤性蛛网膜下'
# 筛选出包含"高血压"的行
filtered_df1 = df1[(df1['diagnosis_name_original'].str.contains('动脉闭塞'))|(df1['diagnosis_name_original'].str.contains('脑梗死'))|(df1['diagnosis_name_original'].str.contains('动脉狭窄'))]
filtered_df2 = df2[(df2['diagnosis_name_original'].str.contains('动脉闭塞'))|(df2['diagnosis_name_original'].str.contains('脑梗死'))|(df2['diagnosis_name_original'].str.contains('动脉狭窄'))]
# # filtered_df1 = df1[((df1['diagnosis_name_original'].str.contains('损伤')) 
# #                    | (df1['diagnosis_name_original'].str.contains('创伤')) |(df1['diagnosis_name_original'].str.contains('挫伤')))& (df1['diagnosis_name_original'].str.contains('颅脑'))
# #                    & (~df1['diagnosis_name_original'].str.contains('恢复期')) &(~df1['diagnosis_name_original'].str.contains('后遗症')) &(~df1['diagnosis_name_original'].str.contains('个人史'))]
# # filtered_df2 = df2[((df2['diagnosis_name_original'].str.contains('损伤')) 
# #                    | (df2['diagnosis_name_original'].str.contains('创伤')) | (df2['diagnosis_name_original'].str.contains('挫伤'))) &(df2['diagnosis_name_original'].str.contains('颅脑'))
# #                    & (~df2['diagnosis_name_original'].str.contains('恢复期')) &(~df2['diagnosis_name_original'].str.contains('后遗症')) &(~df2['diagnosis_name_original'].str.contains('个人史'))]


# # pattern = r'创伤性.*(蛛网膜下腔出血|脑内血肿|硬膜外血肿|硬膜下血肿|轴索损伤|脑疝)'
# # filtered_df1 = df1[(df1['diagnosis_name_original'].str.contains(pattern,na=False,flags=re.IGNORECASE))|(df1['diagnosis_name_original'].str.contains('脑挫伤'))]
# # filtered_df2 = df2[(df2['diagnosis_name_original'].str.contains(pattern,na=False,flags=re.IGNORECASE))|(df2['diagnosis_name_original'].str.contains('脑挫伤'))]
# # 计算这些行中数量的总和
total_count1 = filtered_df1['count'].sum()
total_count2 = filtered_df2['count'].sum()  
print(f"出院包含的{contain_content}的疾病诊断总数量是：{total_count1}")
print(f"入院包含的{contain_content}的疾病诊断总数量是：{total_count2}")


# 统计mimic的disease
import pandas as pd



# 出血性卒中
pattern1 = r'I60|I61|I62'
# 高血压
pattern2 = r'I10|I11|I12|I13|I15'
pattern2  = r'I10'
# 糖尿病
pattern3 = r'E10|E11|E13|E14'
# 肺部感染
pattern4 = r'J10|J11|J12|J13|J14|J15|J16|J17|J18|J20|J21|J22|J98'
# 动脉瘤
pattern5 = r'I71|I72|I67'
# 蛛网膜下腔出血
pattern6 = r'I60'
# 创伤性脑损伤
pattern7 = r'S06'
# 颅内占位性病变
pattern8 = r'D33|C71|D32|D35|D42|D43|C70|C72|C75|C79|R90'
# 缺血性脑血管病
pattern9 = r'I63|I65|I66'
def statistic_diagnosis(pattern):
    # 读取CSV文件
    df1 = pd.read_csv('mimic_ns_diagnosis.csv')
    df2 = pd.read_csv('inspire_ns_diagnosis.csv')
    filtered_df1 = df1[df1['icd_code'].str.contains(pattern,regex=True,na = False)]
    filtered_df2 = df2[df2['icd10_cm'].str.contains(pattern,regex=True,na = False)]
    filtered_df2 = filtered_df2.drop_duplicates(subset = ['hadm_id','icd10_cm'])
    print(filtered_df1)
    print('mimic:',len(filtered_df1))
    print('inspire:',len(filtered_df2))

statistic_diagnosis(pattern2)
# filtered_df1 = df1[((df1['diagnosis_name_original'].str.contains('损伤')) 
#                    | (df1['diagnosis_name_original'].str.contains('创伤')) |(df1['diagnosis_name_original'].str.contains('挫伤')))& (df1['diagnosis_name_original'].str.contains('颅脑'))
#                    & (~df1['diagnosis_name_original'].str.contains('恢复期')) &(~df1['diagnosis_name_original'].str.contains('后遗症')) &(~df1['diagnosis_name_original'].str.contains('个人史'))]
# filtered_df2 = df2[((df2['diagnosis_name_original'].str.contains('损伤')) 
#                    | (df2['diagnosis_name_original'].str.contains('创伤')) | (df2['diagnosis_name_original'].str.contains('挫伤'))) &(df2['diagnosis_name_original'].str.contains('颅脑'))
#                    & (~df2['diagnosis_name_original'].str.contains('恢复期')) &(~df2['diagnosis_name_original'].str.contains('后遗症')) &(~df2['diagnosis_name_original'].str.contains('个人史'))]
import matplotlib.pyplot as plt
def plot_disease():
    df = pd.read_excel(r"C:\Users\liuxiaoli\Desktop\入院出院诊断统计.xlsx", sheet_name='Sheet2')
    df.set_index(df.columns[0],inplace=True)
    df.plot(kind = 'bar',width = 0.8)

    plt.title('Discharge Diagnosis Across Different Datasets')
    plt.xlabel('Discharge diagnosis')
    plt.ylabel('Count')
    # plt.legend(title = '')
    plt.show()
# plot_disease()