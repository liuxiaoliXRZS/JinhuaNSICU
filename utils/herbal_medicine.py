import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm
"""
This script analyzes the distribution of herbal medicine doses for a specific set of herbs using visualizations.
"""
plt.rcParams['font.sans-serif'] = ['SimHei']
df = pd.read_csv('jinhuaNSICU\herbal_medicine.csv',encoding='gbk')

herbs_of_interest = ['甘草','金银花','菊花','三叶青','白芷']

data_to_plot = df[df['medicine_name_CH'].isin(herbs_of_interest)]

plt.figure(figsize=(15,5))

# sns.boxplot(x = 'medicine_name_CH', y = 'dose_herbal', data = data_to_plot)
for i,herb in enumerate(herbs_of_interest, 1):
    plt.subplot(1,len(herbs_of_interest),i)
    sns.histplot(data_to_plot[data_to_plot['medicine_name_CH'] == herb]['dose_herbal'],kde = False,bins = 20)
    plt.xlabel('剂量')
    plt.title(f'{herb} Distribution')
    if i == 1:
        plt.ylabel('频次')
    else:
        plt.ylabel('')
plt.tight_layout()
plt.show()