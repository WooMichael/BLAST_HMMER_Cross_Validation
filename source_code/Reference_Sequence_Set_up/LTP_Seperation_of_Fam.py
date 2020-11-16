# Author Michael Woo
# The way the naming goes is Genera Species  Family
# The goal of this program is to sperate these three rankings into their own directories...
from Bio import SeqIO
import os

LTP_path = "/root/Github/Project_Mendel/Data/Reference_sequences_from_LTP/LTPs132_SSU_compressed.fasta"
Fam_path = "/root/Github/Project_Mendel/Data/Reference_sequences_from_LTP/Family/"
Genera_path = "/root/Github/Project_Mendel/Data/Reference_sequences_from_LTP/Genera/"
Species_path = "/root/Github/Project_Mendel/Data/Reference_sequences_from_LTP/Species/"
Family_ls = list()
Genera_ls = list()
Species_ls = list()
Total_Seqs = 0

for record in SeqIO.parse(LTP_path, "fasta"):
    record_description = str(record.description).split()
    Total_Seqs += 1

    if (len(record_description) == 8):
        Family = record_description.__getitem__(7)
        Species = record_description.__getitem__(6)
        Genera = record_description.__getitem__(5)
        Family_ls.append(Family)
        Species_ls.append(Species)
        Genera_ls.append(Genera)

        # If the directories exist create them if not its okay....
        if not os.path.exists("/root/Github/Project_Mendel/Data/Reference_sequences_from_LTP/Genera/" + Family):
            os.mkdir("/root/Github/Project_Mendel/Data/Reference_sequences_from_LTP/Genera/" + Family)
        if not os.path.exists("/root/Github/Project_Mendel/Data/Reference_sequences_from_LTP/Species/" + Genera):
            os.mkdir("/root/Github/Project_Mendel/Data/Reference_sequences_from_LTP/Species/" + Genera)

        # dedicated path directories
        Genera_Family_path = "/root/Github/Project_Mendel/Data/Reference_sequences_from_LTP/Genera/" + Family + "/"
        Species_Genera_path = "/root/Github/Project_Mendel/Data/Reference_sequences_from_LTP/Species/" + Genera + "/"

        # we want to use  "a" for file opener because we want to append new information to it...
        with open(Fam_path + Family + '.fa', "a") as Family_handle:
            SeqIO.write(record, Family_handle, "fasta")
        with open(Genera_Family_path + Genera + '.fa', "a") as Genera_handle:
            SeqIO.write(record, Genera_handle, "fasta")
        with open(Species_Genera_path + Species + '.fa', "a") as Species_handle:
            SeqIO.write(record, Species_handle, "fasta")

    if (len(record_description) == 9):
        # print(record_description)
        Family = record_description.__getitem__(8)
        Species = record_description.__getitem__(6)
        Genera = record_description.__getitem__(5)
        Family_ls.append(Family)
        Species_ls.append(Species)
        Genera_ls.append(Genera)
        # If the directories exist create them if not its okay....
        if not os.path.exists("/root/Github/Project_Mendel/Data/Reference_sequences_from_LTP/Genera/" + Family):
            os.mkdir("/root/Github/Project_Mendel/Data/Reference_sequences_from_LTP/Genera/" + Family)
        if not os.path.exists("/root/Github/Project_Mendel/Data/Reference_sequences_from_LTP/Species/" + Genera):
            os.mkdir("/root/Github/Project_Mendel/Data/Reference_sequences_from_LTP/Species/" + Genera)

        # dedicated path directories
        Genera_Family_path = "/root/Github/Project_Mendel/Data/Reference_sequences_from_LTP/Genera/" + Family + "/"
        Species_Genera_path = "/root/Github/Project_Mendel/Data/Reference_sequences_from_LTP/Species/" + Genera + "/"

        # we want to use  "a" for file opener because we want to append new information to it...
        with open(Fam_path + Family + '.fa', "a") as Family_handle:
            SeqIO.write(record, Family_handle, "fasta")
        with open(Genera_Family_path + Genera + '.fa', "a") as Genera_handle:
            SeqIO.write(record, Genera_handle, "fasta")
        with open(Species_Genera_path + Species + '.fa', "a") as Species_handle:
            SeqIO.write(record, Species_handle, "fasta")

    if (len(record_description) == 10):
        # print(record_description)
        Family = record_description.__getitem__(9)
        Species = record_description.__getitem__(6)
        Genera = record_description.__getitem__(5)
        Family_ls.append(Family)
        Species_ls.append(Species)
        Genera_ls.append(Genera)
        # If the directories exist create them if not its okay....
        if not os.path.exists("/root/Github/Project_Mendel/Data/Reference_sequences_from_LTP/Genera/" + Family):
            os.mkdir("/root/Github/Project_Mendel/Data/Reference_sequences_from_LTP/Genera/" + Family)
        if not os.path.exists("/root/Github/Project_Mendel/Data/Reference_sequences_from_LTP/Species/" + Genera):
            os.mkdir("/root/Github/Project_Mendel/Data/Reference_sequences_from_LTP/Species/" + Genera)

        # dedicated path directories
        Genera_Family_path = "/root/Github/Project_Mendel/Data/Reference_sequences_from_LTP/Genera/" + Family + "/"
        Species_Genera_path = "/root/Github/Project_Mendel/Data/Reference_sequences_from_LTP/Species/" + Genera + "/"

        # we want to use  "a" for file opener because we want to append new information to it...
        with open(Fam_path + Family + '.fa', "a") as Family_handle:
            SeqIO.write(record, Family_handle, "fasta")
        with open(Genera_Family_path + Genera + '.fa', "a") as Genera_handle:
            SeqIO.write(record, Genera_handle, "fasta")
        with open(Species_Genera_path + Species + '.fa', "a") as Species_handle:
            SeqIO.write(record, Species_handle, "fasta")

    if (len(record_description) == 11):
        Family = record_description.__getitem__(10)
        Species = record_description.__getitem__(6)
        Genera = record_description.__getitem__(5)
        Family_ls.append(Family)
        Species_ls.append(Species)
        Genera_ls.append(Genera)
        # If the directories exist create them if not its okay....
        if not os.path.exists("/root/Github/Project_Mendel/Data/Reference_sequences_from_LTP/Genera/" + Family):
            os.mkdir("/root/Github/Project_Mendel/Data/Reference_sequences_from_LTP/Genera/" + Family)
        if not os.path.exists("/root/Github/Project_Mendel/Data/Reference_sequences_from_LTP/Species/" + Genera):
            os.mkdir("/root/Github/Project_Mendel/Data/Reference_sequences_from_LTP/Species/" + Genera)

        # dedicated path directories
        Genera_Family_path = "/root/Github/Project_Mendel/Data/Reference_sequences_from_LTP/Genera/" + Family + "/"
        Species_Genera_path = "/root/Github/Project_Mendel/Data/Reference_sequences_from_LTP/Species/" + Genera + "/"

        # we want to use  "a" for file opener because we want to append new information to it...
        with open(Fam_path + Family + '.fa', "a") as Family_handle:
            SeqIO.write(record, Family_handle, "fasta")
        with open(Genera_Family_path + Genera + '.fa', "a") as Genera_handle:
            SeqIO.write(record, Genera_handle, "fasta")
        with open(Species_Genera_path + Species + '.fa', "a") as Species_handle:
            SeqIO.write(record, Species_handle, "fasta")
Family_ls = list(dict.fromkeys(Family_ls))
Genera_ls = list(dict.fromkeys(Genera_ls))
Species_ls = list(dict.fromkeys(Species_ls))
with open("/root/Github/Project_Mendel/Data/Reference_Sequences_QQ_check.txt", "w") as handle:
    for tracker, fam in enumerate(Family_ls):
        handle.write(fam + '\t')
        if tracker % 5 == 4:
            handle.write('\n')
    handle.write("Total count of Sequences is : " + str(Total_Seqs))
