import pandas as pd
from pathlib import Path
from datetime import datetime
from datetime import timedelta

### Date and Time Utils

def getToday ():
    today = datetime.today()
    return today

def getYesterday():
    today = getToday ()
    yesterday = today - timedelta(days = 1)
    return yesterday

def getEndDate ():
    yesterday = getToday ()
    return formatDate (yesterday)

def formatDate (date=datetime.today()):
    return date.strftime('%Y-%m-%d')

### CSV, JSON file DF utils

CSV_EXT = '.csv'
def readDfFromCsv (filename):
    if filename is not None:
        completeFilename = filename + CSV_EXT
        return pd.read_csv (filepath_or_buffer = completeFilename)

def writeDfToCsv (df, path, filename='file.csv'):
    Path(path).mkdir(parents=True, exist_ok=True)
    completeFilename = path + filename + CSV_EXT
    df.to_csv(path_or_buf = completeFilename, index=True)

def writeJSON (j, filename = 'file.json' ):
    with open(filename, 'w') as outfile:
        json.dump(j, outfile)

def readJSON (filename):
    f = open (filename)
    j = json.load (f)
    f.close()
    return json.loads (j)
