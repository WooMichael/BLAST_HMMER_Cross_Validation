import os
from Bio import SeqIO

# stream = os.popen(
#     'ls /home/ubuntu/Github/Project_Mendel/Data/Species_Search_Data/Aligned_Reference_Sequences_From_LTP_Species/')
# output = stream.readlines()
# ref_path = "/home/ubuntu/Github/Project_Mendel/Data/Species_Search_Data/Aligned_Reference_Sequences_From_LTP_Species/"
# hmm_path = "/home/ubuntu/Github/Project_Mendel/Data/Species_Search_Data/HMM_Builds_From_Aligned_Sequences_LTP_Species/"

stream = os.popen(
    'ls /root/Github/Project_Mendel/Data/Species_Search_Data/Aligned_Reference_Sequences_From_LTP_Species/')
output = stream.readlines()
ref_path = "/root/Github/Project_Mendel/Data/Species_Search_Data/Aligned_Reference_Sequences_From_LTP_Species/"
hmm_path = "/root/Github/Project_Mendel/Data/Species_Search_Data/HMM_Builds_From_Aligned_Sequences_LTP_Species/"

for fam in output:
    family = str(fam).rstrip('\n')
    path = ref_path + family
    gen_stream = os.popen("ls " + path)
    gen_output = gen_stream.readlines()
    dir_gen_path = hmm_path + family + "/"
    if not os.path.exists(dir_gen_path):
        os.mkdir(dir_gen_path)
    for gen in gen_output:
        hmm_gen = gen.replace('.fa', '.hmm')
        gen_path = path + "/" + gen
        command_line_msa = "hmmbuild " + dir_gen_path + family + "_" + hmm_gen.strip() + " " + gen_path
        print(command_line_msa)
        os.popen(str(command_line_msa))
