import pandas as pd
import json

def readCSV (name):
    if name is not None:
        return pd.read_csv (filepath_or_buffer = name)

def writeCSV (df, name='file.csv'):
    df.to_csv(path_or_buf = name, index=True)

def writeJsonDump (j, name = 'file.json' ):
    with open(name, 'w') as outfile:
        json.dump(j, outfile)

def readJSON (filename):
    f = open (filename)
    j = json.load (f)
    f.close()
    return json.loads (j)
