import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from datetime import datetime
import matplotlib.gridspec as gridspec
import os
csv_file = ['Vital_signs(replaceAndDel).csv','Examination.csv','Laboratory_test.csv','Medication.csv','Surgical_record_front_page.csv','orders.csv']

def onePatientPage(hadm_id, folder_path):
    # Ensure the output directory exists
    output_dir = 'OnePatientv4/'
    os.makedirs(output_dir, exist_ok=True)

    # Get all CSV files in the specified folder
    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

    # Iterate over all CSV files in the folder
    for file_name in csv_files:
        # Construct the file path
        file_path = os.path.join(folder_path, file_name)
        
        # Read the CSV file
        try:
            df = pd.read_csv(file_path,encoding='utf-8')
        except UnicodeDecodeError:
            df = pd.read_csv(file_path,encoding='gbk')
        
        # Filter rows where 'hadm_id' matches the given hadm_id
        filtered_df = df[df['hadm_id'] == hadm_id]
        
        # Save the filtered data to a new CSV file in the output directory
        output_file_path = os.path.join(output_dir, file_name)
        filtered_df.to_csv(output_file_path, index=False)

# Example usage
folder_path = '0802v1'  # Replace with the path to your folder containing CSV files
hadm_id = 'IP06394'  # Replace with your specific hadm_id
# onePatientPage(hadm_id, folder_path)


# for i in range(len(csv_file)):
#     onePatientPage('IP06394',csv_file[i])
'''
************************
绘制  检验  图
************************
'''

# df = pd.read_csv('一位患者的检验.csv')
# # inspection_name = df['inspection_name'].unique()
# # 统计inspection_name的出现次数
# inspection_counts = df['inspection_name_en'].value_counts()

# # 找出出现次数大于10次的元素
# frequent_inspections = inspection_counts[inspection_counts > 18].index.tolist()
# legend = []
# print(frequent_inspections)
# plt.figure(figsize=(10, 5))
# for item in frequent_inspections:
#     if item == 'Bacterial name' or item == 'Actual bicarbonate' \
#         or item == 'Ionic chlorine' or item == 'Ionized calcium' \
#             or item == 'PH' or item == 'Ionic potassium':
#         continue
#     df1 = df[df['inspection_name_en'] == item]
#     df1['report_time_base'] = df1['report_time_base'].apply(lambda x:round(x/60,2))
#     plt.plot(df1['report_time_base'], df1['test_results_quantitative'], marker='o')
#     legend.append(item)

# plt.title('Laboratory_test')
# plt.xlabel('Time after admission to the hospital,hours')
# plt.ylabel('Measurement')
# plt.grid(False)
# plt.legend(legend,fontsize = 'small')
# plt.show()



'''
************************
绘制  检验  图
************************
'''

# df = pd.read_csv('一位患者的检验_uni.csv')
# Date = df['report_time_base']
# Event = df['inspection_type_en']
# # 示例数据
# data = {
#     'Date': Date,
#     'Event': Event,
#     # 'Description': ['Description 1', 'Description 2', 'Description 3', 'Description 4','5','6','7']
# }

# # 创建DataFrame
# df = pd.DataFrame(data)

# # 将日期列转换为NumPy数组
# dates = df['Date'].values
# event_types = df['Event'].unique()
# colors = plt.cm.tab20(range(len(event_types)))

# color_map = dict(zip(event_types,colors))
# print(color_map)
# # 创建绘图
# fig, ax = plt.subplots(figsize=(10, 4))

# # 绘制时间轴
# for event in event_types:
#     event_dates = df[df['Event'] == event]['Date']
#     ax.plot(event_dates,[1]*len(event_dates),'o',markersize = 10,color = color_map[event],label = event)

# # 隐藏y轴
# ax.yaxis.set_visible(False)
# ax.legend(title = 'Events',loc = 'upper center',bbox_to_anchor = (0.5,1.15),ncol = 4)
# # 设置边界和网格
# ax.spines['left'].set_visible(False)
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)
# ax.spines['bottom'].set_position('center')

# # plt.grid(axis='x')
# plt.tight_layout()
# plt.show()





'''
************************
绘制  检查  图
************************
'''

# df = pd.read_csv('一位患者的检查.csv')
# Date = df['examine_time_base'].apply(lambda x:round(x/60,2))
# Event = df['check_type_en']
# # 示例数据
# data = {
#     'Date': Date,
#     'Event': Event,
#     'Description': ['Description 1', 'Description 2', 'Description 3', 'Description 4','5','6','7']
# }

# # 创建DataFrame
# df = pd.DataFrame(data)

# # 将日期列转换为NumPy数组
# dates = df['Date'].values
# event_types = df['Event'].unique()
# colors = plt.cm.tab20(range(len(event_types)))

# color_map = dict(zip(event_types,colors))
# print(color_map)
# # 创建绘图
# fig, ax = plt.subplots(figsize=(10, 4))

# # 绘制时间轴
# for event in event_types:
#     event_dates = df[df['Event'] == event]['Date']
#     ax.plot(event_dates,[1]*len(event_dates),'o',markersize = 10,color = color_map[event],label = event)

# # 隐藏y轴
# ax.yaxis.set_visible(False)
# ax.legend(title = 'Examination',loc = 'upper left',bbox_to_anchor = (0.7,1.05),ncol = 1)
# # 设置边界和网格
# ax.spines['left'].set_visible(False)
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)
# ax.spines['bottom'].set_position('center')

# plt.title('Examination')
# plt.xlabel('Time after admission to the hospital,hours')
# plt.tight_layout()
# plt.show()
# import matplotlib.pyplot as plt


'''
************************
绘制  生命体征  图
************************
'''


# 读取数据
def plot():
    import matplotlib.pyplot as plt
    import matplotlib.gridspec as gridspec
    import pandas as pd
    import numpy as np

    # 读取数据
    df_vitals = pd.read_csv('Onepatientv3/Vital_signs(replaceAndDel).csv',encoding='gbk')
    df_vitals['charttime_base'] = df_vitals['charttime_base'].apply(lambda x: round(x / 60, 2))

    df_vitals = df_vitals.sort_values(by='charttime_base')
    df_tempa = df_vitals[df_vitals['subcategory_name'] == '体温']
    df_resp = df_vitals[df_vitals['subcategory_name'] == '呼吸']
    df_sbp = df_vitals[df_vitals['subcategory_name'] == '收缩压']
    df_pulse = df_vitals[df_vitals['subcategory_name'] == '脉搏']
    df_dbp = df_vitals[df_vitals['subcategory_name'] == '舒张压']
    df_spo2 = df_vitals[df_vitals['subcategory_name'] == '血氧饱和度']

    # 创建图像
    fig = plt.figure(figsize=(15, 10))  # 增加图表宽度
    gs = gridspec.GridSpec(5, 1, height_ratios=[1, 1,1, 1, 0.5], hspace=0.15)  # 调整hspace增加子图之间的距离

    # 设置整体风格
    plt.style.use('seaborn-whitegrid')

    # 绘制带有背景颜色的网格
    def add_colored_background(ax):
        ax.set_facecolor('#f0f8ff')  # 设置背景颜色为浅蓝色
        ax.grid(True, which='both', color='white', linewidth=2)  # 设置网格线的颜色和宽度
        ax.set_axisbelow(True)  # 确保网格线在曲线下面

    # 绘制第一个子图
    # 绘制第一个子图
    ax1 = fig.add_subplot(gs[0])
    add_colored_background(ax1)

    

    # 去掉收缩压和舒张压的marker，填充两条曲线之间的区域
    ax1.fill_between(df_sbp['charttime_base'], df_dbp['value'], df_sbp['value'], color='#D1E7DD', alpha=1, label='Blood Pressure (mmHg)')
    ax1.plot(df_sbp['charttime_base'], df_sbp['value'], color='#D1E7DD', linestyle='-')
    ax1.plot(df_dbp['charttime_base'], df_dbp['value'], color='#D1E7DD', linestyle='-')
    # 绘制其他曲线
    ax1.plot(df_tempa['charttime_base'], df_tempa['value'], marker='o', markersize=3, label='Temperature (\u00B0C)', color='#7B2877')
    ax1.plot(df_resp['charttime_base'], df_resp['value'], marker='s', markersize=3, label='Respiratory (Times/Minute)', color='#8C1C29')
    ax1.plot(df_pulse['charttime_base'], df_pulse['value'], marker='v', markersize=3, label='Pulse (Times/Minute)', color='#0353A2')
    ax1.plot(df_spo2['charttime_base'], df_spo2['value'], marker='h', markersize=3, label='SpO2 (%)', color='#ECA614')
    # 调整图例位置
    ax1.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)

    # 隐藏多余的坐标轴边框
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['bottom'].set_visible(False)
    ax1.spines['left'].set_visible(False)

    # 调整x轴刻度显示
    ax1.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)

    # 设置Y轴标签
    ax1.set_ylabel('Vital signs', fontsize=12, fontweight='bold', color='white', bbox=dict(facecolor='skyblue', edgecolor='none', pad=5))
    ax1.yaxis.set_label_coords(-0.1, 0.5)  # 增加Y轴标签与图表之间的距离

    # 绘制第二个子图
    ax2 = fig.add_subplot(gs[1], sharex=ax1)
    add_colored_background(ax2)
    df_lab = pd.read_csv('Onepatientv3/Laboratory_test.csv')
    df_lab = df_lab.sort_values(by='report_time_base')
    df_lab = df_lab.dropna(subset = ['test_results_quantitative'])
    inspection_counts = df_lab['inspection_name_en'].value_counts()
    frequent_inspections = inspection_counts[inspection_counts > 85].index.tolist()
    frequent_inspections.extend(['Calcium','Creatinine','Glucose','Albumin','Sodium','CHloride','Leukocyte','Potassium'])
    legend = []
    for item in frequent_inspections:
        if item in ['Bacterial name', 'Actual bicarbonate', 'Ionic chlorine', 'Ionized calcium', 'PH']:
            continue
        df1 = df_lab[df_lab['inspection_name_en'] == item]
        df1['report_time_base'] = df1['report_time_base'].apply(lambda x: round(x / 60, 2))
        ax2.plot(df1['report_time_base'], df1['test_results_quantitative'], marker='o',markersize = 3)
        legend.append(item)
    ax2.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    ax2.set_ylabel('Laboratory Test', fontsize=12,fontweight = 'bold', color='white', bbox=dict(facecolor='skyblue', edgecolor='none', pad=5))
    ax2.yaxis.set_label_coords(-0.1, 0.5)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['bottom'].set_visible(False)
    ax2.spines['left'].set_visible(False)
    plt.legend(legend, fontsize='small', bbox_to_anchor=(1.12, 1), borderaxespad=0)  # 将图例放在图表外部
    

    ax3 = fig.add_subplot(gs[2], sharex=ax1)
    add_colored_background(ax3)
    df_med = pd.read_csv('OnePatientv3/Medication.csv')
    df_med = df_med[['medication_trade_name_en','starttime_base','endtime_base']]
    df_ord = pd.read_csv('OnePatientv3/Orders.csv')
    df_ord = df_ord.rename(columns={
        'order_content_en':'medication_trade_name_en',
    })
    df_ord = df_ord[['medication_trade_name_en','starttime_base','endtime_base']]
    df_ord  = df_ord[df_ord['medication_trade_name_en'] == 'Ventilator mechanical ventilation (invasive)']
    df_ord['starttime_base'] = pd.to_numeric(df_ord['starttime_base'],errors='coerce')
    df_ord['endtime_base'] = pd.to_numeric(df_ord['endtime_base'],errors='coerce')
    df_med = pd.concat([df_med,df_ord])
    df_med = df_med.sort_values(by = 'starttime_base')
    print(df_med)
    medications = ['<Danger>Concentrated Sodium Chloride Injection (10%)','Tranexamic acid injection',
                  '(Bangting) White-browed Snake Venom Hemagglutinin for Injection','Mannitol injection',
                  '(Methylprednisolone) Methylprednisolone Sodium Succinate for Injection','Ventilator mechanical ventilation (invasive)']
    med_to_label = {
        '<Danger>Concentrated Sodium Chloride Injection (10%)':'Concentrated Sodium Chloride',
        'Tranexamic acid injection':'Tranexamic acid injection',
        'Mannitol injection':'Mannitol',
        '(Bangting) White-browed Snake Venom Hemagglutinin for Injection':'White-browed Snake Venom Hemagglutinin',
        '(Methylprednisolone) Methylprednisolone Sodium Succinate for Injection':'Methylprednisolone Sodium Succinate',
        'Ventilator mechanical ventilation (invasive)':'Ventilator mechanical ventilation'
    }
    for med in medications:
        med_data = df_med[df_med['medication_trade_name_en'] == med]
        y_label = med_to_label[med]
        print(y_label)
        for _, row in med_data.iterrows():

            ax3.barh(y_label,(row['endtime_base'] - row['starttime_base'])/60, left = row['starttime_base']/60,color = 'steelblue')
            bar_width = (row['endtime_base'] - row['starttime_base'])/60
            # ax3.text(row['starttime_base']/60+bar_width/2,med,str(row['drug_specifications']),va = 'center',ha = 'center',color = 'white',fontweight = 'bold')
    # colors = plt.cm.get_cmap('tab20',df_med['surgery_name_en'].nunique())
    # operation_mapping = {name: i for i, name in enumerate(df_med['surgery_name_en'].unique())}
    # for i, row in df_med.iterrows():
    #     ax3.scatter(row['surgery_endtime_base']/60,operation_mapping[row['surgery_name_en']],color = colors(operation_mapping[row['surgery_name_en']]))
    # ax3.set_yticks(range(len(operation_mapping)))
    # ax3.set_yticklabels(operation_mapping.keys())
    ax3.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    # ax3.yaxis.set_ticks([])
    ax3.yaxis.tick_right()
    ax3.yaxis.set_label_position('right')
    ax3.spines['top'].set_visible(False)
    ax3.spines['right'].set_visible(False)
    ax3.spines['bottom'].set_visible(False)
    ax3.spines['left'].set_visible(False)
    # ax3.spines['bottom'].set_position('center')
    ax3.set_ylabel('treatment', fontsize=12,fontweight = 'bold', color='white', bbox=dict(facecolor='skyblue', edgecolor='none', pad=5))
    ax3.yaxis.set_label_coords(-0.115, 0.5)




    # 绘制第三个子图
    ax4 = fig.add_subplot(gs[3], sharex=ax1)
    add_colored_background(ax4)
    df_surgeries = pd.read_csv('OnePatientv3/Surgical_record_front_page.csv')
    colors = plt.cm.get_cmap('tab20',df_surgeries['surgery_name_en'].nunique())
    operation_mapping = {name: i for i, name in enumerate(df_surgeries['surgery_name_en'].unique())}
    for i, row in df_surgeries.iterrows():
        ax4.scatter(row['surgery_endtime_base']/60,operation_mapping[row['surgery_name_en']],color = colors(operation_mapping[row['surgery_name_en']]))
    ax4.set_yticks(range(len(operation_mapping)))
    ax4.set_yticklabels(operation_mapping.keys())
    ax4.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    # ax3.yaxis.set_ticks([])
    ax4.yaxis.tick_right()
    ax4.yaxis.set_label_position('right')
    ax4.spines['top'].set_visible(False)
    ax4.spines['right'].set_visible(False)
    ax4.spines['bottom'].set_visible(False)
    ax4.spines['left'].set_visible(False)
    # ax3.spines['bottom'].set_position('center')
    ax4.set_ylabel('Surgery', fontsize=12,fontweight = 'bold', color='white', bbox=dict(facecolor='skyblue', edgecolor='none', pad=5))
    ax4.yaxis.set_label_coords(-0.115, 0.5)

    
    # 绘制第四个子图
    ax5 = fig.add_subplot(gs[4], sharex=ax1)
    add_colored_background(ax5)
    df_exams = pd.read_csv('Onepatientv3/Examination.csv')
    Date = df_exams['examine_time_base'].apply(lambda x: round(x / 60, 2))
    Event = df_exams['check_type_en']
    data = {'Date': Date, 'Event': Event}
    df = pd.DataFrame(data)
    dates = df['Date'].values
    event_types = df['Event'].unique()
    colors = plt.cm.tab20(range(len(event_types)))
    color_map = dict(zip(event_types, colors))

    for event in event_types:
        event_dates = df[df['Event'] == event]['Date']
        ax5.plot(event_dates, [1] * len(event_dates), 'o', markersize=10, color=color_map[event], label=event)

    ax5.tick_params(axis='x', which='both', pad = 65)
    ax5.legend(loc='upper left', bbox_to_anchor=(1.02, 1), borderaxespad=0)
    ax5.yaxis.set_ticks([])
    ax5.spines['top'].set_visible(False)
    ax5.spines['right'].set_visible(False)    
    ax5.spines['bottom'].set_position('center')
    ax5.set_ylabel('Examination', fontsize=12,fontweight = 'bold', color='white', bbox=dict(facecolor='skyblue', edgecolor='none', pad=5))
    ax5.yaxis.set_label_coords(-0.1, 0.5)
    ax5.spines['left'].set_visible(False)


    fig.subplots_adjust(right=0.75)  # 调整图表右边距，确保图例完整显示
    ax5.set_xlabel('Time after admission to the hospital (hours)')
    # plt.grid(False)
    plt.savefig('Onepatient.svg',bbox_inches = 'tight')
plot()
