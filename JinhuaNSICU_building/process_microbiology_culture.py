import pandas as pd

df = pd.read_csv('0729v2\microbiology_culture.csv')

df['test_time_base'] = pd.to_numeric(df['test_time_base'],errors = 'coerce')
df = df.groupby(['subject_id','hadm_id']).apply(lambda x:x.sort_values('test_time_base'))

df = df.to_csv('0729v2\microbiology_culture.csv',index= False)
