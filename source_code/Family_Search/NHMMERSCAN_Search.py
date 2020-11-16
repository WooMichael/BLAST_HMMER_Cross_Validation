import os

hmmdb_path = "/Users/mwoo/Documents/2020/BitBucket/16s-subunit-bacteria-hmm-search/Family_DB"
seq_file = "/Users/mwoo/Documents/2020/BitBucket/16s-subunit-bacteria-hmm-search/Data/Metadata/Experimental_Sequences_Kaplan/"
stream = os.popen("ls " + seq_file)
output = stream.readlines()
output_from_search = "/Users/mwoo/Documents/2020/BitBucket/16s-subunit-bacteria-hmm-search/Data/Family_Search_Data/MSA_Scans_From_nhmmerscan/"
counter = 0
for seq in output:
    seq_output_reformat = seq.replace('.fa', '.txt')
    # Always remember to strip the reformats or any variables to ensure that we can run the commands properly
    command_line_nhmmscan_tblout = "nhmmscan --noali --tblout " + output_from_search.strip() + seq_output_reformat.strip() + " " + hmmdb_path.strip() + " " + seq_file.strip() + seq.strip()
    # print(command_line_nhmmscan_tblout)
    print("Processing this sequence file: " + seq.strip())
    os.system(command_line_nhmmscan_tblout)
    counter += 1
    print("So far this many has been scanned: " + str(counter))
print(
    "Scans are in please go into this folder to view each individual hits of each sequence that was queried in the database...")
print("This folder: " + output_from_search)
