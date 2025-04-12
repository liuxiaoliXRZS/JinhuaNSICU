import os
import pandas as pd

def generate_mappings(mapping_file_path):
    # 读取包含所有subject_id和hadm_id的文件
    df = pd.read_csv(mapping_file_path)
    
    # 创建subject_id和hadm_id的映射
    subject_id_mapping = {subject_id: idx + 1 for idx, subject_id in enumerate(df['subject_id'].unique())}
    hadm_id_mapping = {hadm_id: f"IP{str(idx + 1).zfill(5)}" for idx, hadm_id in enumerate(df['hadm_id'].unique())}
    print('subject_id:',subject_id_mapping)
    print('hadm_id:', hadm_id_mapping)
    # 将映射转换为DataFrame并保存到Excel
    subject_id_df = pd.DataFrame(list(subject_id_mapping.items()), columns=['Original', 'Mapped'])
    hadm_id_df = pd.DataFrame(list(hadm_id_mapping.items()), columns=['Original', 'Mapped'])
    
    subject_id_df.to_excel('subject_id_mapping.xlsx', index=False)
    hadm_id_df.to_excel('hadm_id_mapping.xlsx', index=False)
    return subject_id_mapping, hadm_id_mapping

def map_and_save_csv(file_path, output_folder, subject_id_mapping, hadm_id_mapping):
    # 读取csv文件
    df = pd.read_csv(file_path)

    # 应用subject_id映射
    if 'subject_id' in df.columns:
        df['subject_id'] = df['subject_id'].map(subject_id_mapping)

    # 应用hadm_id映射
    if 'hadm_id' in df.columns:
        df['hadm_id'] = df['hadm_id'].map(hadm_id_mapping)

    # 生成新的文件名（保持原文件名）
    new_file_name = os.path.join(output_folder, os.path.basename(file_path))

    # 保存到新的csv文件
    df.to_csv(new_file_name, index=False)

def process_all_csv_files(input_folder, output_folder, mapping_file_path):
    # 生成subject_id和hadm_id的映射
    subject_id_mapping, hadm_id_mapping = generate_mappings(mapping_file_path)

    # 确保输出文件夹存在
    os.makedirs(output_folder, exist_ok=True)

    # 遍历文件夹中的所有csv文件，应用映射并保存为新的文件
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.csv'):
            file_path = os.path.join(input_folder, file_name)
            print('file_path:',file_path)
            map_and_save_csv(file_path, output_folder, subject_id_mapping, hadm_id_mapping)

    print("Mapping and saving completed for all files.")

# 输入文件夹和输出文件夹路径
input_folder = '20240808_neurology/trans_id'
output_folder = '20240808_neurology/trans_id/Finished'
mapping_file_path = '0729v1\Medical_record_front_page.csv'  # 包含所有subject_id和hadm_id的文件

process_all_csv_files(input_folder, output_folder, mapping_file_path)
