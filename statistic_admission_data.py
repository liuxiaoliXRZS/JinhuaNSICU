
import pandas as pd

def analyze_admission_data(df):
    """
    Analyze admission data to calculate statistics about multiple admissions and time spans.
    """
    try:
        # Ensure 'admittime' is in datetime format
        df['admittime'] = pd.to_datetime(df['admittime'], format='%Y%m%d %H:%M:%S', errors='coerce')

        # 1. Count unique admissions per patient
        admission_counts = df.groupby('subject_id')['hadm_id'].nunique()

        # 2. Calculate the number of patients with multiple admissions and total patients
        multiple_admissions_count = admission_counts[admission_counts > 1].count()
        total_patients_count = admission_counts.count()
        print(f'Total number of patients: {total_patients_count}')

        # 3. Calculate the proportion of patients with multiple admissions
        proportion_multiple_admissions = multiple_admissions_count / total_patients_count
        print(f'Proportion of patients with multiple admissions: {proportion_multiple_admissions:.2%}')

        # 4. Filter patients with multiple admissions
        multiple_admission_ids = admission_counts[admission_counts > 1].index
        multiple_admissions_df = df[df['subject_id'].isin(multiple_admission_ids)]

        # 5. Calculate time span between first and last admission for each patient
        grouped = multiple_admissions_df.groupby('subject_id')['admittime']
        first_admission = grouped.min()
        last_admission = grouped.max()
        time_spans = (last_admission - first_admission).dt.total_seconds() / (365.25 * 24 * 3600)

        # 6. Calculate median, quartiles, and maximum time span
        median_span = time_spans.median()
        q1_span = time_spans.quantile(0.25)
        q3_span = time_spans.quantile(0.75)
        max_span = time_spans.max()

        print(f'Median time span: {median_span:.2f} years')
        print(f'First quartile (Q1): {q1_span:.2f} years')
        print(f'Third quartile (Q3): {q3_span:.2f} years')
        print(f'Maximum time span: {max_span:.2f} years')

        # 7. Calculate statistics for the number of admissions for patients with multiple admissions
        multiple_admission_counts = admission_counts[admission_counts > 1]
        median_admissions = multiple_admission_counts.median()
        q1_admissions = multiple_admission_counts.quantile(0.25)
        q3_admissions = multiple_admission_counts.quantile(0.75)

        print(f'Median number of admissions for patients with multiple admissions: {median_admissions}')
        print(f'First quartile (Q1) of admissions: {q1_admissions}')
        print(f'Third quartile (Q3) of admissions: {q3_admissions}')

    except Exception as e:
        print(f"An error occurred during analysis: {e}")

# Example usage
if __name__ == "__main__":
    # Load your data here
    input_file = "./jinhuaNSICU/medical_record_front_page.csv"
    try:
        df = pd.read_csv(input_file)
        analyze_admission_data(df)
    except FileNotFoundError:
        print(f"Error: File {input_file} not found. Please check the file path.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty. Please check the data.")
    except Exception as e:
        print(f"An unexpected error occurred while loading the data: {e}")