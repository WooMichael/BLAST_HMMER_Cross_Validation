import os
from Bio import SeqIO

# stream = os.popen(
#     'ls /home/ubuntu/Github/Project_Mendel/Data/Genera_Search_Data/Aligned_Reference_Sequences_From_LTP_Genera/')
# output = stream.readlines()
# ref_path = "/home/ubuntu/Github/Project_Mendel/Data/Genera_Search_Data/Aligned_Reference_Sequences_From_LTP_Genera/"
# hmm_path = "/home/ubuntu/Github/Project_Mendel/Data/Genera_Search_Data/HMM_Builds_From_Aligned_Sequences_LTP_Genera/"

stream = os.popen(
    'ls /root/Github/Project_Mendel/Data/Genera_Search_Data/Aligned_Reference_Sequences_From_LTP_Genera/')
output = stream.readlines()
ref_path = "/root/Github/Project_Mendel/Data/Genera_Search_Data/Aligned_Reference_Sequences_From_LTP_Genera/"
hmm_path = "/root/Github/Project_Mendel/Data/Genera_Search_Data/HMM_Builds_From_Aligned_Sequences_LTP_Genera/"
for fam in output:
    family = str(fam).rstrip("\n")
    path = ref_path + family
    gen_stream = os.popen("ls " + path)
    gen_output = gen_stream.readlines()
    dir_gen_path = hmm_path + family + "/"
    dir_gen_path = dir_gen_path.rstrip()
    if not os.path.exists(dir_gen_path):
        os.mkdir(dir_gen_path)
    for gen in gen_output:
        hmm_gen = gen.replace('.fa', '.hmm')
        hmm_gen = hmm_gen.strip()
        hmm_build_path = dir_gen_path + family + "_" + hmm_gen
        gen_path = path + "/" + gen.strip()
        command_line_msa = "hmmbuild " + hmm_build_path + " " + gen_path.rstrip()
        print(command_line_msa)
        os.popen(str(command_line_msa))
