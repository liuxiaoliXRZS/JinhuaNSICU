import pandas as pd

def sort_and_save_csv(input_file, output_file):
    """
    Reads a CSV file, sorts the data by 'charttime' in descending order 
    within each group of 'subject_id' and 'hadm_id', and saves the sorted data to a new file.

    Parameters:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to save the sorted CSV file.
    """
    try:
        # Load the data from the input file
        df = pd.read_csv(input_file)
        
        # Group by 'subject_id' and 'hadm_id', then sort each group by 'charttime' in descending order
        df_sorted = (
            df.groupby(['subject_id', 'hadm_id'], group_keys=False)
              .apply(lambda x: x.sort_values('charttime', ascending=False))
        )
        
        # Save the sorted DataFrame to the output file
        df_sorted.to_csv(output_file, index=False)
        print(f"Sorted data has been saved to {output_file}")
    
    except FileNotFoundError:
        print(f"Error: File {input_file} not found. Please check the file path.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty. Please check the data.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def extract_unique_elements(input_file, output_file, target_column):
    """
    从 CSV 文件中提取某一列的唯一元素，并保存到新的 CSV 文件。

    参数：
        input_file (str): 输入 CSV 文件路径。
        output_file (str): 输出 CSV 文件路径。
        target_column (str): 需要提取的目标列名。

    返回：
        None
    """
    try:
        # 读取原始 CSV 文件
        df = pd.read_csv(input_file)

        # 检查目标列是否存在
        if target_column not in df.columns:
            raise ValueError(f"列名 '{target_column}' 不存在于输入文件中！")

        # 提取目标列并去重
        unique_elements = df[target_column].drop_duplicates()

        unique_elements.to_excel(output_file, index=False, header=[target_column])

        print(f"提取完成！唯一元素已保存到 {output_file}")

    except Exception as e:
        print(f"发生错误：{e}")


# 定义映射函数
def map_yes_no_to_english(df, input_col, output_col):

    mapping = {"是": "Yes", "否": "No"}

    df[output_col] = df[input_col].map(mapping)
    
    return df


def replace_column_with_mapping(
    input_csv, output_csv, mapping_xlsx,
    csv_key_column, mapping_old_key_column, mapping_new_key_column
):
    """
    根据映射表替换 CSV 文件中的某一列值。

    参数:
        input_csv (str): 输入 CSV 文件路径。
        output_csv (str): 输出 CSV 文件路径。
        mapping_xlsx (str): 映射表 Excel 文件路径。
        csv_key_column (str): 需要被替换的 CSV 列名。
        mapping_old_key_column (str): 映射表中旧键的列名。
        mapping_new_key_column (str): 映射表中新键的列名。
    """
    df = pd.read_csv(input_csv)
    mapping_df = pd.read_excel(mapping_xlsx)
    mapping_dict = dict(zip(mapping_df[mapping_old_key_column], mapping_df[mapping_new_key_column]))
    df[csv_key_column] = df[csv_key_column].map(mapping_dict).fillna(df[csv_key_column])
    df.to_csv(output_csv, index=False, encoding='utf-8')

# replace_column_with_mapping("chief_complaint.csv","chief_complaint.csv","hadm_id_mapping.xlsx","hadm_id","Original","Mapped")
# 创建 DataFrame
# df = pd.read_csv("0924/patient_expire_hospital.csv")
# df = df[~df["subject_id"].isna()]
# # 调用映射函数
# df = map_yes_no_to_english(df, input_col="expire_flag", output_col="expire_flag_en")

# # 保存为新的 CSV 文件
# df.to_csv("0924/patient_expire_hospital0.csv", index=False, encoding="utf-8-sig")


# 示例调用
input_file = '0924/medical_record_new.csv'  # 输入文件名
output_file = 'trans_columns/E_medical_record_chief_complaint.xlsx'  # 输出文件名
target_column = 'chief_complaint'  # 目标列名

extract_unique_elements(input_file, output_file, target_column)

# Example usage
# if __name__ == "__main__":
#     input_file = './jinhuaNSICU/Daily_progress.csv'
#     output_file = './sorted_Daily_progress.csv'
#     sort_and_save_csv(input_file, output_file)