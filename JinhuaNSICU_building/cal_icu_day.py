import pandas as pd
#  利用transfer表进行计算
def cal_icu_day_transfer():
    # df = pd.read_csv('./dataframe_uni_merge_translated/Transfer.csv')
    # print(df['outtime_base'].dtype)
    # # 按照subject_id和hadm_id进行分组，并对每个分组按照“outtime_base”列进行排序
    # df['outtime_base'] = pd.to_numeric(df['outtime_base'],errors='coerce')
    # df = df.groupby(['subject_id','hadm_id']).apply(lambda x:x.sort_values('outtime_base'))
    # df['intime_base'] = pd.to_numeric(df['intime_base'],errors='coerce')
    # df['intime_base'] = df['intime_base'].fillna(df['outtime_base'])

    # # print(df['intime_base'].tolist())
    # df = df.to_csv('./sorted_Transfer.csv',index = False)
    sort_df = pd.read_csv('./sorted_Transfer.csv')
    # data_dict = {}
    # import csv
    # with open('./dataframe_uni_merge_translated/病案首页.csv',mode = 'r',encoding='utf-8') as file:
    #     reader = csv.DictReader(file)
    #     for row in reader:
    #         key = (str(row['subject_id']),str(row['hadm_id']))
    #         data_dict[key] = row['dischtime_base']

    # dischtime_base_list = []
    # with open('./sorted_Transfer.csv', mode='r', encoding='utf-8') as file:
    #     reader = csv.DictReader(file)
    #     for row in reader:
    #         key = (str(row['subject_id']), str(row['hadm_id']))
    #         if key in data_dict:
    #             dischtime_base_list.append(data_dict[key])
    # df = pd.read_csv('./sorted_Transfer.csv')
    # df['dischtime'] = dischtime_base_list
    # df = df.to_csv('./sorted_Transfer.csv',index = False)

    # print(sort_df)
    grouped = sort_df.groupby(['subject_id','hadm_id'])
    icu_time_list = pd.DataFrame(columns=['subject_id','hadm_id','icu_time'])
    for name,group in grouped:
        group = group.reset_index(drop=True)
        icu_time = 0
        pre = 0
        cur = 0
        for i in range(len(group)):
            
            # print(group['outtime_base'][i])
            if str(group['outtime_base'][i]) == 'nan':
                continue
            cur = group['outtime_base'][i]
            if '重症' in group['out_department'][i]:
                icu_time += (cur - pre)
            pre = group['intime_base'][i]
            if i == len(group) - 1 and '重症' in group['transfer_department'][i]:
                icu_time += (group['dischtime'][i]-group['intime_base'][i])

        icu_time_list = pd.concat([icu_time_list,pd.DataFrame({'subject_id':[name[0]],'hadm_id':[name[1]],'icu_time':[round(icu_time/(24*60),2)]})],ignore_index= True)
        # print(icu_time_list)
    icu_time_list.to_csv('icu_time.csv',index=False)

def cal_icu_day_orders():
    df = pd.read_csv('0802v1\Orders.csv')
    icu_df = df[df['order_content'] == 'ICU单元治疗']
    icu_df['starttime_base'] = pd.to_numeric(icu_df['starttime_base'],errors='coerce')
    icu_df['endtime_base'] = pd.to_numeric(icu_df['endtime_base'],errors='coerce')
    icu_df['icu_time'] = (icu_df['endtime_base'] - icu_df['starttime_base'])
    icu_time_per_hadm = icu_df.groupby('hadm_id')['icu_time'].sum() / (60 * 24)
    print(icu_time_per_hadm)
    result_df = icu_time_per_hadm.reset_index()
    result_df.columns = ['hadm_id','icu_time']

    result_df.to_csv('icu_time_new.csv',index=False)

    median_time = result_df['icu_time'].median()
    q1_time = result_df['icu_time'].quantile(0.25)
    q3_time = result_df['icu_time'].quantile(0.75)
    print('ICU中位数为:',median_time)
    print('第一四分位数：',q1_time)
    print('第三分位数：',q3_time)
cal_icu_day_orders()
    
    


        
