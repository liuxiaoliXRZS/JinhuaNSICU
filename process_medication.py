import pandas as pd

df = pd.read_csv('0729v2\Medication.csv')

df['starttime_base'] = pd.to_numeric(df['starttime_base'],errors = 'coerce')
df = df.groupby(['subject_id','hadm_id']).apply(lambda x:x.sort_values('starttime_base'))

df = df.to_csv('0729v2\Medication.csv',index= False)
