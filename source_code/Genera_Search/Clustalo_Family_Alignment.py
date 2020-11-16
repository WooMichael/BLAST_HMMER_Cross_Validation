import os

from Bio import SeqIO

# stream is the variable that allows me to use the command line in python
stream = os.popen('ls /home/ubuntu/Github/Project_Mendel/Data/Reference_sequences_from_LTP/Genera/ ')
# the output is saved
output = stream.readlines()
# `print(output)
# this is where the alignment begins
for gen in output:
    # each gen is the name of the folder by family
    # print(gen)
    # path to the directory of families
    gen = gen.strip()
    path_gen = '/home/ubuntu/Github/Project_Mendel/Data/Reference_sequences_from_LTP/Genera/' + str(gen)
    # we do a list of the genera in that specific family
    gen_stream = os.popen('ls ' + path_gen)
    gen_output = gen_stream.readlines()
    dir_gen_path = "/home/ubuntu/Github/Project_Mendel/Data/Genera_Search_Data/Aligned_Reference_Sequences_From_LTP_Genera/" + gen
    # print(dir_gen_path)
    # if not os.path.exists(dir_gen_path):
    #       os.mkdir(dir_gen_path)
    # for each sequence in the genera depending of the family
    for genera in gen_output:
        # print(genera)
        genera = str(genera).strip()
        # this is the path from the Data Reference lib
        path = path_gen + '/' + genera
        # you want to use this when there are more than 1 sequence in a fasta file
        clustalo_command_line = "clustalo -i " + path + " " + "-o " + "/home/ubuntu/Github/Project_Mendel/Data/Genera_Search_Data/Aligned_Reference_Sequences_From_LTP_Genera/" + gen + "/" + gen + "_" + genera
        # you want to use this when there are ONLY 1 sequence in a fasta file
        copy_file_command_line = "cp " + path + " " + "/home/ubuntu/Github/Project_Mendel/Data/Genera_Search_Data/Aligned_Reference_Sequences_From_LTP_Genera/" + gen + "/" + gen + "_" + genera
        # print(clustalo_command_line)
        # counter counts the amount of sequences in the fasta file...
        counter = 0
        # If the directories exist create them if not its okay...
        if not os.path.exists(dir_gen_path):
            os.mkdir(dir_gen_path)
        for seq_record in SeqIO.parse(path, "fasta"):
            # counts how many record (sequences) there are in the family record
            counter += 1
            # print(counter)
        # after counting the records we then choose which command we want to run below
        if (counter == 1):
            print("only 1 seq")
            os.popen(copy_file_command_line)
        if (counter > 1):
            print("more than 1 seq")
            os.popen(clustalo_command_line)

#  print(path)
