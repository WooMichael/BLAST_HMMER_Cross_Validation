import os
import sys

stream = os.popen(
    "ls /root/Github/Project_Mendel/Data/Species_Search_Data/HMM_Builds_From_Aligned_Sequences_LTP_Species/")
output = stream.readlines()
counter = 0
for directory in output:
    # print(directory)
    directory_stream = os.popen(
        "ls /root/Github/Project_Mendel/Data/Species_Search_Data/HMM_Builds_From_Aligned_Sequences_LTP_Species/" + directory)
    directory_output = directory_stream.readlines()
    # print(genera)
    path = "/root/Github/Project_Mendel/Data/Species_Search_Data/HMM_Builds_From_Aligned_Sequences_LTP_Species/" + directory.strip() + "/"
    writable_path = "/root/Github/Project_Mendel/Data/Species_Search_Data/Database/" + directory.strip()
    # print(path)
    # print(writable_path)
    os.popen("touch " + writable_path)
    os.popen("cat " + path + "* > " + writable_path)
    counter += 1
    # os.popen("hmmpress " + writable_path)
    print("So far only " + str(counter) + " has been OPENED")
counter = 0
for directory in output:
    # print(directory)
    directory_stream = os.popen(
        "ls /root/Github/Project_Mendel/Data/Species_Search_Data/HMM_Builds_From_Aligned_Sequences_LTP_Species/" + directory)
    directory_output = directory_stream.readlines()
    # print(genera)
    path = "/root/Github/Project_Mendel/Data/Species_Search_Data/HMM_Builds_From_Aligned_Sequences_LTP_Species/" + directory.strip() + "/"
    writable_path = "/root/Github/Project_Mendel/Data/Species_Search_Data/Database/" + directory.strip()
    # print(path)
    # print(writable_path)
    # os.popen("touch " + writable_path)
    # os.popen("cat " + path + "* > " + writable_path)
    counter += 1
    os.system("hmmpress " + writable_path)
    print("So far only " + str(counter) + " has been done HMMPRESS")
