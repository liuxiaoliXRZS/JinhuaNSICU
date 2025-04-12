import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import gridspec 
"""
This function is used to plot boxplots of hospital stay lengths, combining data from different datasets 
(JinhuaNSICU, MIMIC-IV, and INSPIRE) for total distribution, gender distribution, and age group distribution. 
The final chart will display the distribution of hospital stay lengths across various categories (total, gender, age groups) 
for each dataset.
"""
def plot_combined_boxplot():
    data_jinhua = pd.read_csv('jinhuaNSICU\medical_record_front_page.csv')
    data_mimic = pd.read_csv('mimic_ns_info.csv')
    data_in = pd.read_csv('inspire_ns_info.csv')

    data_jinhua = data_jinhua[data_jinhua['length_stay'] < 60]
    data_mimic = data_mimic[data_mimic['los_hospital_day'] < 60]
    data_in = data_in[data_in['los_hospital_day'] < 60]

    data_jinhua['Dataset'] = 'JinhuaNSICU'
    data_mimic['Dataset'] = 'MIMIC-IV'
    data_in['Dataset'] = 'INSPIRE'

    data_jinhua['Gender'] = data_jinhua['patient_gender_en']
    data_mimic['Gender'] = data_mimic['gender'].map({'M': 'Male', 'F': 'Female'})
    data_in['Gender'] = data_in['sex'].map({'M': 'Male', 'F': 'Female'})

    age_groups = [(16, 65), (65, 80), (80, 200)]
    
    def categorize_age(age):
        for i, (lower, upper) in enumerate(age_groups):
            if lower <= age < upper:
                if upper == 200:
                     return '[80,)'
                return f'[{lower},{upper})'
        return None

    data_jinhua['Age Group'] = data_jinhua['age'].apply(categorize_age)
    data_mimic['Age Group'] = data_mimic['age'].apply(categorize_age)
    data_in['Age Group'] = data_in['age'].apply(categorize_age)

    combined_data = pd.concat([
        pd.DataFrame({'Length of stay': data_jinhua['length_stay'], 'Category': 'Total', 'Dataset': 'JinhuaNSICU'}),
        pd.DataFrame({'Length of stay': data_mimic['los_hospital_day'], 'Category': 'Total', 'Dataset': 'MIMIC-IV'}),
        pd.DataFrame({'Length of stay': data_in['los_hospital_day'], 'Category': 'Total', 'Dataset': 'INSPIRE'}),
        pd.DataFrame({'Length of stay': data_jinhua['length_stay'], 'Category': 'Male', 'Dataset': 'JinhuaNSICU', 'Gender': data_jinhua['Gender']}),
        pd.DataFrame({'Length of stay': data_mimic['los_hospital_day'], 'Category': 'Male', 'Dataset': 'MIMIC-IV', 'Gender': data_mimic['Gender']}),
        pd.DataFrame({'Length of stay': data_in['los_hospital_day'], 'Category': 'Male', 'Dataset': 'INSPIRE', 'Gender': data_in['Gender']}),
        pd.DataFrame({'Length of stay': data_jinhua['length_stay'], 'Category': 'Female', 'Dataset': 'JinhuaNSICU', 'Gender': data_jinhua['Gender']}),
        pd.DataFrame({'Length of stay': data_mimic['los_hospital_day'], 'Category': 'Female', 'Dataset': 'MIMIC-IV', 'Gender': data_mimic['Gender']}),
        pd.DataFrame({'Length of stay': data_in['los_hospital_day'], 'Category': 'Female', 'Dataset': 'INSPIRE', 'Gender': data_in['Gender']}),
        pd.DataFrame({'Length of stay': data_jinhua['length_stay'], 'Category': data_jinhua['Age Group'], 'Dataset': 'JinhuaNSICU'}),
        pd.DataFrame({'Length of stay': data_mimic['los_hospital_day'], 'Category': data_mimic['Age Group'], 'Dataset': 'MIMIC-IV'}),
        pd.DataFrame({'Length of stay': data_in['los_hospital_day'], 'Category': data_in['Age Group'], 'Dataset': 'INSPIRE'})
    ])

    combined_data = combined_data.dropna(subset=['Category'])

    age_order = ['[16,65)', '[65,80)', '[80,)']
    combined_data['Category'] = pd.Categorical(combined_data['Category'], categories=['Total', 'Male', 'Female'] + age_order, ordered=True)

    fontsize = 17

    plt.figure(figsize=(12, 8), dpi=100)
    sns.boxplot(x='Category', y='Length of stay', hue='Dataset', data=combined_data,showfliers=False)
    custom_labels = ['Total', 'Male', 'Female', 'Age Group [16,65)', 'Age Group [65,80)', 'Age Group [80,)']
    plt.xticks(ticks=range(len(custom_labels)), labels=custom_labels, fontsize=16, rotation=45)
    plt.xlabel('Category (Total, Gender, Age)', fontsize=fontsize)
    plt.ylabel('Length of hospital stay (Days)', fontsize=fontsize)
    plt.xticks(fontsize=fontsize, rotation=45)  
    plt.yticks(fontsize=fontsize)
    plt.legend(fontsize=fontsize)
    plt.tight_layout()

    plt.savefig('figure/住院时长箱线图_combined.svg', bbox_inches='tight', pad_inches=0.1)

if __name__ == '__main__':
    plot_combined_boxplot()