from Bio import SeqIO
sequence_path = '.../Data/Metadata/All_Kaplan_Sequences.fa'
sep_sequence_path = ".../Data/Metadata/Experimental_Sequences_Kaplan/"
counter = 0
for record in SeqIO.parse(sequence_path, "fasta"):
    path_to_save = sep_sequence_path + record.id + ".fa"
    #SeqIO.write(record, path_to_save, "fasta")
    counter += 1
    print(record.id)
    print(record.seq)
    print(len(record.seq))

# print(record)
print("Seperation Complete...")
print("you have seperated this many sequences : " + str(counter))
