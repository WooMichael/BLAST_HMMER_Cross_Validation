from Bio import SeqIO
import pandas as pd
import os
import numpy as np

# Global Variables
all_kap_sequence_path = '../Data/Metadata/All_Kaplan_Sequences.fa'
seq_kap_path = "../Data/Metadata/Experimental_Sequences_Kaplan/"
top_result_path = "../Data/Genera_Search_Data/Top_Hits_Scans/Scanned_Results.csv"
scan_path = "../Data/Genera_Search_Data/MSA_Scans_From_nhmmerscan/"
counter = 0
top_hits_txt_list = os.listdir(scan_path)
final_tuple = []
# Getting the path for the output of each sequence
for name in top_hits_txt_list:
    path = scan_path + name
    with open(path, "r") as file1:
        line = file1.readlines()
        arr = np.array(line)
        arr = arr[2:3]
        array = str(arr).split()
        new_array = np.array(array)
        if (len(new_array) > 1):
            query_name = new_array[2]
            top_hit = new_array[0]
            e_score = new_array[12]
            bit_score = new_array[13]
            query_name = str(query_name).strip("'[]")
            top_hit = str(top_hit).strip("'[]")
            e_score = str(e_score).strip("'[]")
            bit_score = str(bit_score).strip("'[]")
            # print(query_name, top_hit, e_score, bit_score)
            final_tuple.append(query_name + "," + top_hit + "," + e_score + "," + bit_score + ",")
        else:
            pass
with open("Genera_Top_Hits.csv", "w") as file:
    file.write("Query Name,Top Hit,E-Value,Bit Score,Sequence Count,Total As,Total Ts,Total Cs,Total Gs,Total Ns  \n")

wp = "Genera_Top_Hits.csv"

with open(top_result_path, "r") as file2:
    df1 = pd.read_csv(file2)
    # print(df1.head())
for record in SeqIO.parse(all_kap_sequence_path, "fasta"):
    path_to_save = seq_kap_path + record.id + ".fa"
    # SeqIO.write(record, path_to_save, "fasta")
    counter += 1
    total_a = 0
    total_t = 0
    total_c = 0
    total_g = 0
    total_n = 0
    for letter in record.seq:
        if (letter == 'A'):
            total_a += 1
        elif (letter == 'T'):
            total_t += 1
        elif (letter == 'C'):
            total_c += 1
        elif (letter == 'G'):
            total_g += 1
        elif (letter == 'N'):
            total_n += 1
    for group in final_tuple:
        group = group.split(",")[0:4]
        if (record.id == group[0]):
            group.append(str(len(record.seq)))
            group.append(str(total_a))
            group.append(str(total_t))
            group.append(str(total_c))
            group.append(str(total_g))
            group.append(str(total_n))
            group = str(group)
            group = group.replace("'", "").strip("[]")
            print(group)
            with open("Genera_Top_Hits.csv", "a") as file:
                file.write(group + '\n')
print("Seperation Complete...")
print("you have seperated this many sequences : " + str(counter))