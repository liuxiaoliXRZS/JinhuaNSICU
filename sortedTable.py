import pandas as pd

df = pd.read_csv('./dataframe_uni_merge_translated/Daily_progress.csv')
# print(df['outtime_base'].dtype)
# 按照subject_id和hadm_id进行分组，并对每个分组按照“outtime_base”列进行排序
df['charttime'] = pd.to_datetime(df['charttime'],format = '%Y%m%d %H:%M:%S')
df = df.groupby(['subject_id','hadm_id']).apply(lambda x:x.sort_values('charttime',ascending = False))
df.to_csv('./dataframe_uni_merge_translated_sorted/Daily_progress.csv',index=False)


# df = pd.read_csv('./dataframe_uni_merge_translated_sorted/Daily_progress.csv')
# grouped = df.groupby(['subject_id','hadm_id'])
# halfDayRecord = pd.DataFrame(columns=['subject_id','hadm_id','charttime','course_details','course_theme'])

# for name,group in grouped:
#     group = group.reset_index(drop=True)
#     dischtime = group['charttime_base'][0]
#     for i in range(len(group)):
#         if str(group['charttime_base'][i]) == 'nan' or str(group['charttime_base'][i]) == ' ' :continue
#         # 提取出院时间半天内的数据
#         if (int(dischtime) - int(group['charttime_base'][i])) < 720:
#             halfDayRecord = pd.concat([halfDayRecord,pd.DataFrame({'subject_id':[name[0]],'hadm_id':[name[1]],
#                                                                    'charttime':[group['charttime'][i]],
#                                                                    'course_details':[group['course_details'][i]],
#                                                                    'course_theme':[group['course_theme'][i]],
#                                                                    })],ignore_index= True)
# halfDayRecord.to_csv('./dataframe_uni_merge_translated_sorted/Daily_progress_halfDayRecord.csv',index=False)


# import pandas as pd

# # 读取两个CSV文件
# df1 = pd.read_csv('./temp/statistic_death_part1.csv',encoding='gbk')
# df2 = pd.read_csv('./temp/statistic_death_part4.csv')
# df1 = df1[df1['death_flag'] != 1]
# df2 = df2[df2['order_content'] != '死亡']
# # 提取subject_id列
# subject_ids_1 = df1[['subject_id']]
# subject_ids_2 = df2[['subject_id']]

# merged_df = pd.concat([df1[['subject_id', 'hadm_id']], df2[['subject_id', 'hadm_id']]])

# # 去除重复的subject_id，保留第一个出现的项
# # keep='first' 表示保留第一个出现的重复项，你也可以选择 'last' 或者 False
# unique_merged_df = merged_df.drop_duplicates(subset='subject_id', keep='first')

# # 保存到新的CSV文件中，不包含索引
# unique_merged_df.to_csv('unique_subject_id_hadm_id.csv', index=False)


# import pandas as pd


# 读取两个CSV文件
# df1 = pd.read_csv('./dataframe_uni_merge_translated_sorted/Daily_progress_halfDayRecord.csv') 
# df2 = pd.read_csv('./temp/unique_subject_id_hadm_id.csv')  
# # df2 = df2[df2['death_flag'] != 1]
# # 假设df1中的列名为subject_id和hadm_id，df2中也有这些列
# # 使用merge函数根据subject_id和hadm_id合并两个DataFrame
# merged_df = pd.merge(df1, df2, on =['subject_id','hadm_id'],how='right')

# # 如果你只想根据条件检索，不合并，可以使用以下代码：
# # mask = (df2['subject_id'] == df1['subject_id']) & (df2['hadm_id'] == df1['hadm_id'])
# # filtered_df = df2[mask]

# # 保存到新的CSV文件
# merged_df.to_csv('./dataframe_uni_merge_translated_sorted/Daily_progress_halfDayRecord_Death.csv', index=False)