import pandas as pd

# Define input and output file paths
input_file = "./jinhuaNSICU/medical_record_front_page.csv"
output_file = "./statistic.csv"

def process_medical_records(input_file, output_file):
    """
    Process medical records data:
    - Parse admission time as datetime.
    - Sort by admission time.
    - Remove duplicate subject IDs, keeping the first occurrence.
    - Calculate age in years and length of hospital stay in days.
    - Add a binary column for hospital death.
    - Save the processed data to a CSV file.
    """
    try:
        # Load the CSV file
        df = pd.read_csv(input_file)
        
        # Parse 'admittime' column as datetime and sort by admission time
        df['admittime'] = pd.to_datetime(df['admittime'], errors='coerce')
        df = df.sort_values(by='admittime')
        
        # Remove duplicate rows based on 'subject_id', keeping the first occurrence
        df_unique = df.drop_duplicates(subset="subject_id", keep="first")
        
        # Select relevant columns for further processing
        selected_data = df_unique[['subject_id', 'patient_gender_en', 'age', 'dischtime_base', 'admission_route', 'discharge_type']]
        
        # Convert age from days to years (rounded to 1 decimal place)
        selected_data['age'] = selected_data['age'].apply(lambda x: round(x / 365, 1))
        
        # Calculate length of hospital stay in days (rounded to 2 decimal places)
        selected_data['los_hospital_day'] = selected_data['dischtime_base'].apply(lambda x: round(x / (24 * 60), 2))
        
        # Drop the 'dischtime_base' column as it's no longer needed
        selected_data = selected_data.drop('dischtime_base', axis=1)
        
        # Add a binary column 'death_hosp' indicating whether the discharge type is "死亡" (death)
        selected_data['death_hosp'] = selected_data['discharge_type'].apply(lambda x: 1 if x == "死亡" else 0)
        
        # Drop the 'discharge_type' column as it's no longer needed
        selected_data = selected_data.drop('discharge_type', axis=1)
        
        # Save the processed data to a new CSV file
        selected_data.to_csv(output_file, index=False)
        print(f"Processed data has been saved to {output_file}")
    
    except FileNotFoundError:
        print(f"Error: File {input_file} not found. Please check the file path.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty. Please check the data.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    process_medical_records(input_file, output_file)