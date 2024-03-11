""" 
Author: Justin Krieg
Year: 2023
Description: This script analyses sequences of numbers to derive key stastistics on the radial arm maze as calculated through this study: Tarantino IS, Sharp RF, Geyer MA, et al. Working memory span capacity improved by a D2 but not D1 receptor family agonist. Behav Brain Res 2011;219(2):181–188; doi: 10.1016/j.bbr.2010.12.037.
"""
import pandas as pd
import re
import os

file_path = "~/Downloads/"
input_csv = "input.csv" 
output_csv = "output.csv" 


def total_arms(seq):
    return len(str(seq))

def total_repeated_entries(seq):
    number_dict = {i: 0 for i in range(10)}
    sum_repeated_entries = 0
    for digit in seq:
        if digit.isdigit():
            number_dict[int(digit)] += 1
    for num_in_dict in number_dict:
        if number_dict[num_in_dict] >= 2:
            sum_repeated_entries +=1
    return sum_repeated_entries

def non_baited_entries(seq, nb1, nb2):
    number_dict = {i: 0 for i in range(10)}
    sum_repeated_entries = 0
    for digit in seq:
        if digit.isdigit():
            number_dict[int(digit)] += 1
    sum_repeated_entries = number_dict[nb1] + number_dict[nb2]
    return sum_repeated_entries

def Best_RM(seq,nb1,nb2):
    substituted_seq1 = re.sub(str(nb1), "A", str(seq))
    substituted_seq2 = re.sub(str(nb2), "A", substituted_seq1)
    substituted_seq = re.sub('[0-9]', "B", substituted_seq2)
    segments = substituted_seq.split('A')
    output_list = list(map(len, segments))
    return max(output_list)

def replace_tail(s, target, replacement):
    try:
        pos = s.index(target)
    except ValueError:
        return s
    pos += len(target)
    head = s[:pos]
    tail = s[pos:]
    return head + tail.replace(target, replacement)

def Best_WM(seq):
    seq_str = str(seq)
    for char in set(seq_str):
        if seq_str.count(char) > 1:
            seq_str = replace_tail(seq_str, char, "A")
    substituted_seq = re.sub('[0-9]', "B", seq_str)
    segments = substituted_seq.split('A')
    output_list = list(map(len, segments))
    return max(output_list)

if os.path.exists(file_path + input_csv):
    df = pd.read_csv(file_path)
    df["Total_Arms"] = df.apply(lambda x : total_arms(x['Sequence']), axis=1)
    df["Working_Memory_Errors"] = df.apply(lambda x : total_repeated_entries(x['Sequence']), axis=1)
    df["Non_Baited_Entries"] = df.apply(lambda x : non_baited_entries(x['Sequence'], x['Non_Baited_Arm_1'],x['Non_Baited_Arm_2']), axis=1)
    df["Best_RM"] = df.apply(lambda x : Best_RM(x['Sequence'], x['Non_Baited_Arm_1'],x['Non_Baited_Arm_2']), axis=1)
    df["Best_RM_Percent"] = df.apply(lambda x: x["Best_RM"]/x["Total_Arms"], axis=1)
    df["Best_WM"] = df.apply(lambda x : Best_WM(x['Sequence']), axis=1)
    df["Best_WM_Percent"] = df.apply(lambda x: x["Best_WM"]/x["Total_Arms"], axis=1)
    df["WM_%"] = df.apply(lambda x: x["Working_Memory_Errors"]/x["Total_Arms"], axis=1)
    df["RM_%"] = df.apply(lambda x: x["Non_Baited_Entries"]/x["Total_Arms"], axis=1)
    print(df)
    df.to_csv(file_path + output_csv)
else:
    print("Input file does not exist")
