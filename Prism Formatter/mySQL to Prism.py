""" 
Author: Justin Krieg
Year: 2023
Description: Graphpad prism (10) uses an unconventional data format layout, requiring a subject per column, and experimental conditions grouped into sets of columns. This is a particularly unusual layout compared to the way most mysql data is layed out. This script converts long data into this prism format. 
"""

import pandas as pd
import numpy as np
import os

file_path = "/Users/Justin/Downloads/"
input_csv = "Result_17.csv" 
group_factor = "Animal_Group"
subject = "Animal_ID"
Row_factor_name = "ROI"


def add_rows(x:pd.DataFrame):
    new_index = range(count)
    x = x.reset_index(drop=True)
    y = x.reindex(new_index)
    return y

print (file_path + input_csv)
if os.path.exists(file_path + input_csv):
    df = pd.read_csv(file_path + input_csv)
    df = df.rename(columns={group_factor: "group_factor", subject:"subject", Row_factor_name: "row_factor"})
    df = df.sort_values(by=['group_factor', 'row_factor'])
    count = df.groupby(['group_factor', 'row_factor']).count()
    count = count['subject'].max()
    append_rows = df.groupby(['group_factor', 'row_factor']).apply(add_rows).reset_index(drop=True)
    data_columns = [col for col in append_rows.columns if col not in ['group_factor', 'subject', "row_factor"]]

    for column_name in data_columns:
        df_split = pd.DataFrame()
        selected_columns = append_rows[['group_factor', 'subject', 'row_factor', column_name]].copy()
        selected_columns.columns = ['group_factor', 'subject', 'row_factor', column_name]
        selected_columns['row_factor'].fillna(method='ffill', inplace=True)
        selected_columns['group_factor'].fillna(method='ffill', inplace=True)
        selected_columns.fillna('PLACEHOLDER', inplace=True)
        df_split = selected_columns.pivot_table(columns=['group_factor', 'subject'], index='row_factor', aggfunc='first', fill_value=np.nan).reset_index()
        df_split.replace('PLACEHOLDER', np.nan, inplace=True)
        df_split = df_split.rename(columns={"PLACEHOLDER": np.NaN})
        df_split.columns = df_split.columns.droplevel(level=0)
        df_split.columns = pd.Index([np.nan if x == 'nan' else x for x in df_split.columns])
        print (df_split)
        df_split.to_csv(file_path + column_name + ".csv", header=True, index=False)
else:
    print("Input file does not exist")
