import pandas as pd

import os
rootdir = os.getcwd()
extensions = ('.xpt', '.XPT')

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        ext = os.path.splitext(file)[-1].lower()
        filename = os.path.splitext(file)[0]
        if ext in extensions:
            df = pd.read_sas(os.path.join(subdir, file))
            itr = pd.read_sas(os.path.join(subdir, file), chunksize=100000)
            for chunk in itr:
                print(filename + '.csv')
                df.to_csv (filename + '.csv', float_format='%.10f', index=False)