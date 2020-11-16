import os

from Bio import SeqIO

# stream is the variable that allows me to use the command line in python
stream = os.popen('ls /home/ubuntu/Github/Project_Mendel/Data/Reference_sequences_from_LTP/Species/ ')
# the output is saved
output = stream.readlines()
# `print(output)
# this is where the alignment begins
for spec in output:
    # each gen is the name of the folder by family
    # print(gen)
    # path to the directory of families
    spec = spec.strip()
    path_gen = '/home/ubuntu/Github/Project_Mendel/Data/Reference_sequences_from_LTP/Species/' + str(spec)
    # we do a list of the genera in that specific family
    spec_stream = os.popen('ls ' + path_gen)
    spec_output = spec_stream.readlines()
    # for each sequence in the genera depending of the family
    for specie in spec_output:
        # print(genera)
        specie = str(specie).strip()
        # this is the path from the Data Reference lib
        path = path_gen + '/' + specie
        # you want to use this when there are more than 1 sequence in a fasta file
        clustalo_command_line = "clustalo -i " + path + " " + "-o " + "/home/ubuntu/Github/Project_Mendel/Data/Species_Search_Data/Aligned_Reference_Sequences_From_LTP_Species/" + spec + "/" + spec + "_" + specie
        # you want to use this when there are ONLY 1 sequence in a fasta file
        copy_file_command_line = "cp " + path + " " + "/home/ubuntu/Github/Project_Mendel/Data/Species_Search_Data/Aligned_Reference_Sequences_From_LTP_Species/" + spec + "/" + spec + "_" + specie
        # print(clustalo_command_line)
        # counter counts the amount of sequences in the fasta file...
        counter = 0
        # If the directories exist create them if not its okay....
        dir_spec_path = "/home/ubuntu/Github/Project_Mendel/Data/Species_Search_Data/Aligned_Reference_Sequences_From_LTP_Species/" + spec + "/"
        if not os.path.exists(dir_spec_path):
            os.mkdir(dir_spec_path)
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
