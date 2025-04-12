import pandas as pd

df = pd.read_csv('0903v1/Diagnosis.csv')

filtered_df = df[df['diagnosis_name_original'].str.contains('20',na = False)]

def remove_text_after_first_space(text):
    space_index = text.find(' ')

    if space_index != -1:
        return text[:space_index]
    else:
        return text
    
filtered_df['diagnosis_name_original'] = filtered_df['diagnosis_name_original'].apply(remove_text_after_first_space)
df.update(filtered_df)

df.to_csv('0903v1/Diagnosis(remove).csv',index=False)

