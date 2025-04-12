import pandas as pd

def cal_icu_day_orders():
    """
    Calculate the total ICU time for each hospital admission (hadm_id),
    and compute the median and quartiles.
    Save the results to a CSV file and print the statistics.
    """
    df = pd.read_csv('jinhuaNSICU\Orders.csv')
    icu_df = df[df['order_content'] == 'ICU单元治疗']
    icu_df['starttime_base'] = pd.to_numeric(icu_df['starttime_base'],errors='coerce')
    icu_df['endtime_base'] = pd.to_numeric(icu_df['endtime_base'],errors='coerce')
    icu_df['icu_time'] = (icu_df['endtime_base'] - icu_df['starttime_base'])
    icu_time_per_hadm = icu_df.groupby('hadm_id')['icu_time'].sum() / (60 * 24)

    result_df = icu_time_per_hadm.reset_index()
    result_df.columns = ['hadm_id','icu_time']

    result_df.to_csv('icu_time_new.csv',index=False)

    median_time = result_df['icu_time'].median()
    q1_time = result_df['icu_time'].quantile(0.25)
    q3_time = result_df['icu_time'].quantile(0.75)
    # Print statistical results
    print(f"Median ICU time: {median_time:.2f} days")
    print(f"First quartile: {q1_time:.2f} days")
    print(f"Third quartile: {q3_time:.2f} days")

if __name__ == '__main__':
    cal_icu_day_orders()