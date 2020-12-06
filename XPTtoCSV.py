import pandas as pd

df = pd.read_sas('path/filename')
itr = pd.read_sas('path/filename', chunksize=100000)
for chunk in itr:
    df.to_csv ('csvExport.csv', float_format='%.10f', index=False)