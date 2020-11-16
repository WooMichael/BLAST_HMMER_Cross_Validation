import os
# path of the aligned references
path_aligned = "/Users/mwoo/Documents/2020/BitBucket/16s-subunit-bacteria-hmm-search/Data/Family_Search_Data/Aligned_Reference_Sequences_From_LTP_Family/"
stream = os.popen('ls ' + path_aligned)
output = stream.readlines()
hmm_path = "/Users/mwoo/Documents/2020/BitBucket/16s-subunit-bacteria-hmm-search/Data/Family_Search_Data/HMM_Builds_From_Aligned_Sequences_LTP_Family/"
# this loop will go through all the families that have been aligned and will build HMM for each family
for fam in output:
    family = str(fam).strip()
    path = path_aligned + family
    hmm_family = family.replace('.fa', '.hmm')
    command_line_msa = "hmmbuild " + hmm_path + hmm_family + " " + path_aligned + family
    print(command_line_msa)
    os.system(str(command_line_msa))
#Once we are done with building a HMM profiles for each bacterial family we must create a database that is indexed
os.system("cat /Users/mwoo/Documents/2020/BitBucket/16s-subunit-bacteria-hmm-search/Data/Family_Search_Data/HMM_Builds_From_Aligned_Sequences_LTP_Family/* > Family_DB")
os.system("hmmpress Family_DB")