import os

hmmdb_path = "../Data/Species_Search_Data/Database/"
seq_file = "../Data/Metadata/Experimental_Sequences_Kaplan/"
output_from_search = "../Data/Species_Search_Data/MSA_Scans_From_nhmmerscan/"
with open(seq_file,"r") as file1:
    print(file1.readlines())
exit(12313)
# EC2
# hmmdb_path = "/home/ubuntu/Github/Database/Species_DB"
# # you have to seperate each fasta sequence to its own file before running the hmmscan... brb....to be continued...
# # Usage: hmmscan [-options] <hmmdb> <seqfile>.
# seq_file = "/home/ubuntu/Github/Project_Mendel/Data/Metadata/Experimental_Sequences_Kaplan/"
# stream = os.popen("ls " + seq_file)
# output = stream.readlines()
# output_from_search = "/home/ubuntu/Github/Project_Mendel/Data/Species_Search_Data/MSA_Scans_From_nhmmerscan/"

counter = 0
for seq in output:
    # print(seq)
    seq_output_reformat = seq.replace('.fa', '.txt')
    # bash_script = "bash Script_for_Searching.fs %s %s" % (seq_output_reformat, seq)
    # Always remember to strip the reformats or any variables to ensure that we can run the commands properly
    command_line_nhmmscan_tblout = "nhmmscan --noali --tblout " + output_from_search.strip() + seq_output_reformat.strip() + " " + hmmdb_path.strip() + " " + seq_file.strip() + seq.strip()
    # print(command_line_nhmmscan_tblout)
    print("Processing this sequence file: " + seq.strip())
    os.system(command_line_nhmmscan_tblout)
    print(command_line_nhmmscan_tblout)
    counter += 1
    print("So far this many has been scanned: " + str(counter))
print(
    "Scans are in please go into this folder to view each individual hits of each sequence that was queried in the database...")
print("This folder: " + output_from_search)
