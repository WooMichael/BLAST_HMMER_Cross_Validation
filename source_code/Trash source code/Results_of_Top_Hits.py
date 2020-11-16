import pandas as pd
path_spec = "../../Data/Species_Search_Data/Top_Hits_Scans/Scanned_Results.csv"
df = pd.read_csv(path_spec)
print(df.head())
