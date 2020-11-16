import os

scan_path = "/Users/mwoo/Documents/2020/BitBucket/16s-subunit-bacteria-hmm-search/Data/Family_Search_Data/MSA_Scans_From_nhmmerscan/"
stream = os.popen('ls ' + scan_path)
output = stream.readlines()
top_hit_output = "/Users/mwoo/Documents/2020/BitBucket/16s-subunit-bacteria-hmm-search/Data/Family_Search_Data/Top_Hits_Scans/"
with open(top_hit_output + "Scanned_Results.csv", "a") as file:
    file.write("Query Name, Top Hit, E-Value, Bit Score \n")
    file.close()

for fam in output:
    path = scan_path + fam.strip()
    with open(path, 'r') as handler:
        top_hit = handler.readlines()[2:3]
        top_hit_line = str(top_hit).split()
        if (len(top_hit_line) > 1):
            target_name_family = top_hit_line.__getitem__(0).strip("[").strip("'")
            query_name = top_hit_line.__getitem__(2)
            e_value = top_hit_line.__getitem__(12)
            bit_score = top_hit_line.__getitem__(13)
            print(target_name_family, query_name, e_value, bit_score)
            with open(top_hit_output + "Scanned_Results.csv", "a") as file:
                file.write(query_name + ',' + target_name_family + ',' + e_value + ',' + bit_score + '\n')
                file.close()
        if (len(top_hit_line) == 1):
            print("Scan did not show no hits")
