import pandas as pd
df = pd.read_csv('0729v2\Medical_record_front_page.csv')

df['admittime'] = pd.to_datetime(df['admittime'],format = '%Y%m%d %H:%M:%S')
df = df.groupby(['subject_id']).apply(lambda x:x.sort_values('admittime',ascending = False))
df = df.drop_duplicates(subset='subject_id', keep='first')
# df.to_csv('dataframe_uni_merge_translated_sorted\Medical_record_front_page.csv',index=False)
Subject_hadm_id = dict(zip(df['subject_id'], df['hadm_id']))


df = pd.read_csv('0729v2\Patient.csv')

df['hadm_id'] = df['subject_id'].map(Subject_hadm_id)

cols = df.columns.tolist()
index = cols.index('subject_id')
cols.insert(index + 1,cols.pop(cols.index('hadm_id')))
df = df[cols]

df.to_csv('0729v3\Patient.csv',index=False)