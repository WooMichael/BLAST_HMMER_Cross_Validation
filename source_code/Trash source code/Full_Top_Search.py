import os
# Family path
path_hits_family = open("/root/Github/Project_Mendel/Data/Family_Search_Data/Top_Hits_Scans/Scanned_Results.csv", "r")
lines_fam = path_hits_family.readlines()[1:]
# Genera path
path_hits_genera = open("/root/Github/Project_Mendel/Data/Genera_Search_Data/Top_Hits_Scans/Scanned_Results.csv", "r")
lines_gen = path_hits_genera.readlines()[1:]
# Species path
# Species Database
path_species = "/root/Github/Project_Mendel/Data/Species_Search_Data/Database/"
# experimental sequences
seq_file = "~/Github/Project_Mendel/Data/Metadata/Experimental_Sequences_Kaplan/"
stream = os.popen("ls " + seq_file)
output = stream.readlines()
output_from_search = "~/Github/Project_Mendel/Data/Species_Search_Data/MSA_Scans_From_nhmmerscan/"
counter = 0
# for line in lines_fam:
#     # the assumption is that the family search has already been done
#     print(line)
#     line = line.split(',')
#     id = line.__getitem__(0)
#     family = line.__getitem__(1)
#     e_score = line.__getitem__(2)
#     bit_score = line.__getitem__(3)
#     print("Identifying " + str(id))
#     # genera search
for line_gen in lines_gen:
    print(line_gen)
    line_gen = line_gen.split(",")
    id = line_gen.__getitem__(0)
    hit = line_gen.__getitem__(1)
    hit = hit.split('_')
    family = hit.__getitem__(0)
    genera = hit.__getitem__(1)
    # print(genera)
    # print(line_gen)
    # print(seq)
    seq_output_reformat = id.replace('.fa', '.txt')
    # bash_script = "bash Script_for_Searching.fs %s %s" % (seq_output_reformat, seq)
    # Always remember to strip the reformats or any variables to ensure that we can run the commands properly
    command_line_nhmmscan_tblout = "nhmmscan --noali --tblout " + output_from_search.strip() + seq_output_reformat.strip()+'.txt' + " " + path_species + str(
        genera).strip() + " " + seq_file.strip() + id.strip()+'.fa'
    # print(command_line_nhmmscan_tblout)
    print(command_line_nhmmscan_tblout)
    print("Processing this sequence file: " + id.strip())
    os.system(command_line_nhmmscan_tblout)
    counter += 1
    print("So far this many has been scanned: " + str(counter))
    print(
        "Scans are in please go into this folder to view each individual hits of each sequence that was queried in the database...")
    print("This folder: " + output_from_search)
