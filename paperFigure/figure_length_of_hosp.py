import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import gridspec 
"""
This function generates three sets of density plots to visualize the distribution of hospital stay lengths 
from different datasets (JinhuaNSICU, MIMIC-IV, and INSPIRE). The density plots are categorized by total distribution, 
gender (male and female), and age groups. Each plot compares the distributions across the three datasets
"""
def plot_hosp_length_diff_dataset():
    data_jinhua = pd.read_csv('jinhuaNSICU\medical_record_front_page.csv')
    data_mimic = pd.read_csv('mimic_ns_info.csv')
    data_in = pd.read_csv('inspire_ns_info.csv')
    
    # 过滤住院时长小于60天的记录
    data_jinhua = data_jinhua[data_jinhua['length_stay'] < 60]
    data_mimic = data_mimic[data_mimic['los_hospital_day'] < 60]
    data_in = data_in[data_in['los_hospital_day'] < 60]
    
    # 设置全局字体和线条宽度
    fontsize = 17  
    linewidth = 2.5
    
    # 使用 rcParams 设置全局字体大小
    plt.rcParams.update({'font.size': fontsize})
    
    # 图1：不同数据集的住院时长密度图
    plt.figure(figsize=(6, 8), dpi=100)
    sns.kdeplot(data_jinhua['length_stay'], 
                shade=False, color="#01a2d9", label="JinhuaNSICU",
                alpha=1, linewidth=linewidth)
    sns.kdeplot(data_mimic['los_hospital_day'], 
                shade=False, color="#dc2624", label="MIMIC-IV",
                alpha=1, linewidth=linewidth)
    sns.kdeplot(data_in['los_hospital_day'], 
                shade=False, color="#649E7D", label="INSPIRE",
                alpha=1, linewidth=linewidth)
    
    plt.xlabel('Length of hospital stay (Days)', fontsize=fontsize)
    plt.ylabel('Density', fontsize=fontsize)
    plt.xticks(fontsize=fontsize)
    plt.yticks(fontsize=fontsize)
    plt.xlim(0, 60)
    plt.legend(fontsize=fontsize)
    plt.tight_layout()
    plt.title('Total', fontsize=fontsize)
    plt.savefig('figure/住院时长密度图.svg', bbox_inches='tight', pad_inches=0.1)
    
    # 图2：按性别区分的住院时长密度图
    plt.figure(figsize=(12, 8), dpi=100)
    
    # 提取各性别数据
    data_jinhua_male = data_jinhua[data_jinhua['patient_gender_en'] == 'Male']
    data_jinhua_female = data_jinhua[data_jinhua['patient_gender_en'] == 'Female']
    data_mimic_male = data_mimic[data_mimic['gender'] == 'M']
    data_mimic_female = data_mimic[data_mimic['gender'] == 'F']
    data_in_male = data_in[data_in['sex'] == 'M']
    data_in_female = data_in[data_in['sex'] == 'F']

    plt.subplot(1, 2, 1)
    sns.kdeplot(data_jinhua_male['length_stay'], 
                shade=False, color="#01a2d9", label="JinhuaNSICU",
                alpha=1, linewidth=linewidth)
    sns.kdeplot(data_mimic_male['los_hospital_day'], 
                shade=False, color="#dc2624", label="MIMIC-IV",
                alpha=1, linewidth=linewidth)
    sns.kdeplot(data_in_male['los_hospital_day'], 
                shade=False, color="#649E7D", label="INSPIRE",
                alpha=1, linewidth=linewidth)
    plt.title('Male', fontsize=fontsize)
    plt.xlabel('Length of hospital stay (Days)', fontsize=fontsize)
    plt.ylabel('Density', fontsize=fontsize)
    plt.xticks(fontsize=fontsize)
    plt.yticks(fontsize=fontsize)
    plt.legend(fontsize=fontsize)
    plt.xlim(0, 60)

    plt.subplot(1, 2, 2)
    sns.kdeplot(data_jinhua_female['length_stay'], 
                shade=False, color="#01a2d9", label="JinhuaNSICU",
                alpha=1, linewidth=linewidth)
    sns.kdeplot(data_mimic_female['los_hospital_day'], 
                shade=False, color="#dc2624", label="MIMIC-IV",
                alpha=1, linewidth=linewidth)
    sns.kdeplot(data_in_female['los_hospital_day'], 
                shade=False, color="#649E7D", label="INSPIRE",
                alpha=1, linewidth=linewidth)
    plt.title('Female', fontsize=fontsize)
    plt.xlabel('Length of hospital stay (Days)', fontsize=fontsize)
    plt.xticks(fontsize=fontsize)
    plt.yticks(fontsize=fontsize)
    plt.xlim(0, 60)
    plt.legend(fontsize=fontsize)
    
    plt.tight_layout()
    plt.savefig('figure/男女住院时长密度图.svg', bbox_inches='tight', pad_inches=0.1)

    # 图3：按年龄段的住院时长密度图
    plt.figure(figsize=(18, 8), dpi=100)
    
    # 定义年龄分组
    age_groups = [(16, 65), (65, 80), (80, 200)]
    
    # 分类年龄组
    def categorize_age(age):
        for i, (lower, upper) in enumerate(age_groups):
            if lower <= age < upper:
                return i
        return None

    # 将年龄组分类添加到数据中
    data_jinhua['Age Group'] = data_jinhua['age'].apply(categorize_age)
    data_mimic['Age Group'] = data_mimic['age'].apply(categorize_age)
    data_in['Age Group'] = data_in['age'].apply(categorize_age)

    for i in range(len(age_groups)):
        plt.subplot(1, 3, i+1)
        
        sns.kdeplot(data_jinhua[data_jinhua['Age Group'] == i]['length_stay'], 
                    shade=False, color="#01a2d9", label="JinhuaNSICU",
                    alpha=1, linewidth=linewidth)
        sns.kdeplot(data_mimic[data_mimic['Age Group'] == i]['los_hospital_day'], 
                    shade=False, color="#dc2624", label="MIMIC-IV",
                    alpha=1, linewidth=linewidth)
        sns.kdeplot(data_in[data_in['Age Group'] == i]['los_hospital_day'], 
                    shade=False, color="#649E7D", label="INSPIRE",
                    alpha=1, linewidth=linewidth)
        
        if i == 2:
            plt.title('Age [80,)', fontsize=fontsize)
        elif i == 1:
            plt.title('Age [65,80)', fontsize=fontsize)
        else:
            plt.title('Age [16,65)', fontsize=fontsize)
        
        plt.xlabel('Length of hospital stay (Days)', fontsize=fontsize)
        plt.xticks(fontsize=fontsize)
        plt.yticks(fontsize=fontsize)
        plt.xlim(0, 60)
        plt.legend(fontsize=fontsize)
    
    # 最终调整布局并保存图形
    plt.tight_layout()
    plt.savefig('figure/不同年龄住院时长密度图.svg', bbox_inches='tight', pad_inches=0.1)

if __name__ == '__main__':
    plot_hosp_length_diff_dataset()