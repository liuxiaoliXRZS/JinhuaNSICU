import pandas as pd
import matplotlib.pyplot as plt


data_jinhua = pd.read_csv('jinhua_neurology.csv',encoding='gbk')
data_eicu = pd.read_csv('eicu_neurology.csv')
data_mimic = pd.read_csv('mimic_neurology.csv')
data_sicdb = pd.read_csv('sicdb_neurology.csv')
# 创建年龄分类
bins = [0, 45, 65, 80, float('inf')]
labels = ['<=45', '45-65', '65-80', '80+']
plot_labels = ['jinhua','eicu','mimic','sicdb']
# 将年龄数据分组
data_jinhua['age_group'] = pd.cut(data_jinhua['age'], bins=bins, labels=labels, right=False)
data_eicu['age_group'] = pd.cut(data_eicu['age'], bins=bins, labels=labels, right=False)
data_mimic['age_group'] = pd.cut(data_mimic['age'], bins=bins, labels=labels, right=False)
data_sicdb['age_group'] = pd.cut(data_sicdb['age'], bins=bins, labels=labels, right=False)
# 统计每个年龄组的频数
age_counts_jinhua = data_jinhua['age_group'].value_counts().reindex(labels)
print(age_counts_jinhua)
age_counts_eicu = data_eicu['age_group'].value_counts().reindex(labels)
age_counts_mimic = data_mimic['age_group'].value_counts().reindex(labels)
age_counts_sicdb = data_sicdb['age_group'].value_counts().reindex(labels)

group1 = [age_counts_jinhua['<=45']/data_jinhua.shape[0],age_counts_eicu['<=45']/data_eicu.shape[0],age_counts_mimic['<=45']/data_mimic.shape[0],age_counts_sicdb['<=45']/data_sicdb.shape[0]]
group2 = [age_counts_jinhua['45-65']/data_jinhua.shape[0],age_counts_eicu['45-65']/data_eicu.shape[0],age_counts_mimic['45-65']/data_mimic.shape[0],age_counts_sicdb['45-65']/data_sicdb.shape[0]]
group3 = [age_counts_jinhua['65-80']/data_jinhua.shape[0],age_counts_eicu['65-80']/data_eicu.shape[0],age_counts_mimic['65-80']/data_mimic.shape[0],age_counts_sicdb['65-80']/data_sicdb.shape[0]]
group4 = [age_counts_jinhua['80+']/data_jinhua.shape[0],age_counts_eicu['80+']/data_eicu.shape[0],age_counts_mimic['80+']/data_mimic.shape[0],age_counts_sicdb['80+']/data_sicdb.shape[0]]
print(group1,group2,group3,group4)
# 计算每个部分的相对频率
total_counts = age_counts_jinhua + age_counts_eicu + age_counts_mimic + age_counts_sicdb
age_proportions_jinhua = age_counts_jinhua / total_counts
age_proportions_eicu = age_counts_eicu / total_counts
age_proportions_mimic = age_counts_mimic / total_counts
age_proportions_sicdb = age_counts_sicdb / total_counts

# 绘制直方图
plt.figure(figsize=(10, 6))
plt.bar(plot_labels, group1, color='skyblue', label='<=45')
plt.bar(plot_labels, group2, color='orange', label='45-65', bottom=group1)
plt.bar(plot_labels, group3, color='pink', label='65-80', bottom=[x + y for x, y in zip(group1, group2)])
plt.bar(plot_labels, group4, color='purple', label='80+', bottom=[x + y + z for x, y, z in zip(group1, group2,group3)])
plt.xlabel('four different datasets', fontsize=20)
plt.ylabel('Proportion', fontsize=20)
plt.title('Age Distribution Proportions')
plt.legend(loc='upper left')

# 保存图像文件
plt.savefig('4Hosp_age_proportions.png')



# data_jinhua = pd.read_csv('jinhua_neurology.csv',encoding='gbk')
# data_eicu = pd.read_csv('eicu_neurology.csv')
# data_mimic = pd.read_csv('mimic_neurology.csv')
# data_sicdb = pd.read_csv('sicdb_neurology.csv')
# # 创建年龄分类
# bins = [0,1, 3, 7, float('inf')]
# labels = ['<=1', '1-3', '3-7', '7+']
# plot_labels = ['jinhua','eicu','mimic','sicdb']
# # 将年龄数据分组
# data_jinhua['los_hospital_day_group'] = pd.cut(data_jinhua['los_hospital_day'], bins=bins, labels=labels, right=False)
# data_eicu['los_hospital_day_group'] = pd.cut(data_eicu['los_hospital_day'], bins=bins, labels=labels, right=False)
# data_mimic['los_hospital_day_group'] = pd.cut(data_mimic['los_hospital_day'], bins=bins, labels=labels, right=False)
# data_sicdb['los_hospital_day_group'] = pd.cut(data_sicdb['los_hospital_day'], bins=bins, labels=labels, right=False)
# # 统计每个年龄组的频数
# age_counts_jinhua = data_jinhua['los_hospital_day_group'].value_counts().reindex(labels)
# print(age_counts_jinhua)
# age_counts_eicu = data_eicu['los_hospital_day_group'].value_counts().reindex(labels)
# age_counts_mimic = data_mimic['los_hospital_day_group'].value_counts().reindex(labels)
# age_counts_sicdb = data_sicdb['los_hospital_day_group'].value_counts().reindex(labels)

# group1 = [age_counts_jinhua['<=1']/data_jinhua.shape[0],age_counts_eicu['<=1']/data_eicu.shape[0],age_counts_mimic['<=1']/data_mimic.shape[0],age_counts_sicdb['<=1']/data_sicdb.shape[0]]
# group2 = [age_counts_jinhua['1-3']/data_jinhua.shape[0],age_counts_eicu['1-3']/data_eicu.shape[0],age_counts_mimic['1-3']/data_mimic.shape[0],age_counts_sicdb['1-3']/data_sicdb.shape[0]]
# group3 = [age_counts_jinhua['3-7']/data_jinhua.shape[0],age_counts_eicu['3-7']/data_eicu.shape[0],age_counts_mimic['3-7']/data_mimic.shape[0],age_counts_sicdb['3-7']/data_sicdb.shape[0]]
# group4 = [age_counts_jinhua['7+']/data_jinhua.shape[0],age_counts_eicu['7+']/data_eicu.shape[0],age_counts_mimic['7+']/data_mimic.shape[0],age_counts_sicdb['7+']/data_sicdb.shape[0]]
# print(group1,group2,group3,group4)
# # 计算每个部分的相对频率
# total_counts = age_counts_jinhua + age_counts_eicu + age_counts_mimic + age_counts_sicdb
# age_proportions_jinhua = age_counts_jinhua / total_counts
# age_proportions_eicu = age_counts_eicu / total_counts
# age_proportions_mimic = age_counts_mimic / total_counts
# age_proportions_sicdb = age_counts_sicdb / total_counts

# # 绘制直方图
# plt.figure(figsize=(10, 6))
# plt.bar(plot_labels, group1, color='skyblue', label='<=1')
# plt.bar(plot_labels, group2, color='orange', label='1-3', bottom=group1)
# plt.bar(plot_labels, group3, color='pink', label='3-7', bottom=[x + y for x, y in zip(group1, group2)])
# plt.bar(plot_labels, group4, color='purple', label='7+', bottom=[x + y + z for x, y, z in zip(group1, group2,group3)])
# plt.xlabel('four different datasets', fontsize=20)
# plt.ylabel('Proportion', fontsize=20)
# plt.title('lost_hospital_day Distribution Proportions')
# plt.legend(loc='upper left')

# # 保存图像文件
# plt.savefig('4Hosp_lost_hos_day_proportions.png')
# plt.show()