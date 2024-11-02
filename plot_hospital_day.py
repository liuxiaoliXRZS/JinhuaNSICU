import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def add_colored_background(ax):
    ax.set_facecolor('#f0f8ff')  # 设置背景颜色为浅蓝色
    ax.grid(True, which='both', color='white', linewidth=2)  # 设置网格线的颜色和宽度
    ax.set_axisbelow(True)  # 确保网格线在曲线下面

def jinhua_length_of_hosp():
    # 读取CSV文件
    file_path = '0802v1\Medical_record_front_page.csv'  # 替换为你的文件路径
    data = pd.read_csv(file_path)
    data = data[data['length_stay']< 60]
    # 假设你的数据中有两列：'Gender' 和 'Length_of_Stay'
    # 你可能需要根据你的实际列名进行修改
    male_data = data[data['patient_gender_en'] == 'Male']['length_stay']
    female_data = data[data['patient_gender_en'] == 'Female']['length_stay']

    male_mean = male_data.mean()
    female_mean = female_data.mean()

    # 创建子图
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

    # 绘制男性住院时长的直方图
    axes[0].hist(male_data, bins=50, alpha=0.7, color='#000080',rwidth = 0.8)
    add_colored_background(axes[0])
    axes[0].axvline(male_mean,color = 'k',linestyle = 'dashed',linewidth = 1)
    axes[0].text(male_mean + 1,axes[0].get_ylim()[1] * 0.9,f'Mean:{male_mean:.2f}',color = 'black')
    axes[0].set_title('Male')
    axes[0].set_xlabel('Days of hospital stay (days)')
    axes[0].set_ylabel('Count')
    axes[0].spines['top'].set_visible(False)
    axes[0].spines['right'].set_visible(False)
    axes[0].spines['bottom'].set_visible(False)
    axes[0].spines['left'].set_visible(False)
    # 绘制女性住院时长的直方图
    axes[1].hist(female_data, bins=50, alpha=0.7, color='#000080',rwidth = 0.8)
    add_colored_background(axes[1])
    axes[1].axvline(female_mean,color = 'k',linestyle = 'dashed',linewidth = 1)
    axes[1].text(female_mean + 1,axes[1].get_ylim()[1] * 0.9,f'Mean:{female_mean:.2f}',color = 'black')
    axes[1].set_title('Female')
    axes[1].set_xlabel('Days of hospital stay (days)')
    axes[1].set_ylabel('Count')
    axes[1].spines['top'].set_visible(False)
    axes[1].spines['right'].set_visible(False)
    axes[1].spines['bottom'].set_visible(False)
    axes[1].spines['left'].set_visible(False)
    # 调整子图之间的间距
    plt.tight_layout()

    # 显示图表
    plt.show()

def plot_hosp_length_diff_dataset():
    data_jinhua = pd.read_csv('0802v1\Medical_record_front_page.csv')
    data_mimic = pd.read_csv('mimic_ns_info.csv')
    data_in = pd.read_csv('inspire_ns_info.csv')
    data_jinhua = data_jinhua[data_jinhua['length_stay']< 60]
    data_mimic = data_mimic[data_mimic['los_hospital_day']< 60]
    data_in = data_in[data_in['los_hospital_day']< 60]
    plt.figure(figsize=(10, 8), dpi=80)
    sns.kdeplot(data_jinhua['length_stay'], 
            shade=False,
            color="#01a2d9",
            label="JINHUA",
            alpha=1)
    sns.kdeplot(data_mimic['los_hospital_day'], 
            shade=False,
            color="#dc2624",
            label="MIMIC-IV",
            alpha=1)
    sns.kdeplot(data_in['los_hospital_day'], 
            shade=False,
            color="#649E7D",
            label="INSPIRE",
            alpha=1)
    plt.xlabel('Length of hospital stay (Days)')
    plt.xlim(0, 60)
    plt.legend()    
    plt.savefig('figure/住院时长密度图.svg',bbox_inches = 'tight')
    plt.figure(figsize=(14, 8), dpi=80)
    data_jinhua_male = data_jinhua[data_jinhua['patient_gender_en'] == 'Male']
    data_jinhua_female = data_jinhua[data_jinhua['patient_gender_en'] == 'Female']
    data_mimic_male = data_mimic[data_mimic['gender'] == 'M']
    data_mimic_female = data_mimic[data_mimic['gender'] == 'F']
    data_in_male = data_in[data_in['sex'] == 'M']
    data_in_female = data_in[data_in['sex'] == 'F']
    
    plt.subplot(1, 2, 1)
    sns.kdeplot(data_jinhua_male['length_stay'], 
            shade=False,
            color="#01a2d9",
            label="JINHUA",
            alpha=1)
    sns.kdeplot(data_mimic_male['los_hospital_day'], 
            shade=False,
            color="#dc2624",
            label="MIMIC-IV",
            alpha=1)
    sns.kdeplot(data_in_male['los_hospital_day'], 
            shade=False,
            color="#649E7D",
            label="INSPIRE",
            alpha=1)
    plt.title('Male')
    plt.xlabel('Length of hospital stay (Days)')
    plt.xlim(0, 60)
    plt.subplot(1, 2, 2)
    sns.kdeplot(data_jinhua_female['length_stay'], 
            shade=False,
            color="#01a2d9",
            label="JINHUA",
            alpha=1)
    sns.kdeplot(data_mimic_female['los_hospital_day'], 
            shade=False,
            color="#dc2624",
            label="MIMIC-IV",
            alpha=1)
    sns.kdeplot(data_in_female['los_hospital_day'], 
            shade=False,
            color="#649E7D",
            label="INSPIRE",
            alpha=1)
    

    plt.xlim(0, 60)
    plt.xlabel('Length of hospital stay (Days)')
    plt.legend()
    plt.title('Female')
    plt.tight_layout()
    plt.savefig('figure/男女住院时长密度图.svg',bbox_inches = 'tight')
    plt.figure(figsize=(18, 8), dpi=80)
    # Define the age groups
    age_groups = [(16, 65), (65, 80), (80, 200)]

    # Function to categorize age into groups
    def categorize_age(age):
        for i, (lower, upper) in enumerate(age_groups):
            if lower <= age < upper:
                return i
        return None

    # Add age group column to each DataFrame
    data_jinhua['Age Group'] = data_jinhua['age'].apply(categorize_age)
    data_mimic['Age Group'] = data_mimic['age'].apply(categorize_age)
    data_in['Age Group'] = data_in['age'].apply(categorize_age)
    for i in range(len(age_groups)):
        plt.subplot(1, 3,i+1)
        sns.kdeplot(data_jinhua[data_jinhua['Age Group'] == i]['length_stay'], 
            shade=False,
            color="#01a2d9",
            label="JINHUA",
            alpha=1)
        sns.kdeplot(data_mimic[data_mimic['Age Group'] == i]['los_hospital_day'], 
                shade=False,
                color="#dc2624",
                label="MIMIC-IV",
                alpha=1)
        sns.kdeplot(data_in[data_in['Age Group'] == i]['los_hospital_day'], 
                shade=False,
                color="#649E7D",
                label="INSPIRE",
                alpha=1)
        if i == 2:
            plt.title('Age [80,)')
        elif i == 1:
            plt.title('Age [65,80)')
        else:
            plt.title('Age [16,65)')
        plt.legend()
        plt.xlabel('Length of hospital stay (Days)')
        plt.xlim(0, 60)
        plt.tight_layout()
        plt.savefig('figure/不同年龄住院时长密度图.svg',bbox_inches = 'tight')
    # plt.show()

plot_hosp_length_diff_dataset()
