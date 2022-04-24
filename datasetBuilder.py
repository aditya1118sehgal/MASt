import pandas as pd
from yFin import *
from constants import tickers, paths
from visualize import plotChart
from utils import writeDfToCsv, readDfFromCsv, formatDate
from pathlib import Path

def buildCompleteDatasetBtc (filename = '{}-{}'.format('BTC-USD', formatDate())):
    timeInterval = 'monthly'
    filePath = '{}{}{}{}/'.format (paths['basePath'], paths['csvPath'], paths['cryptoPath'], timeInterval)
    df = None
    print (filePath + filename+'.csv')
    if not Path(filePath + filename+'.csv').is_file():
        print ('no file => pull data')
        r = pullCryptoData ()
        writeDfToCsv (r , filePath, filename)
        r = readDfFromCsv (filePath + filename)
        h = readDfFromCsv ('data/historical-monthly').drop (['adjclose'], axis = 1)
        print (h)
        print (r)
        df = pd.concat ([h, r])
        df = addSMA (df, 20)
        df = addExtensionSMA (df, 20)
        writeDfToCsv (df, filePath, filename)
    else:
        df = readDfFromCsv (filePath + filename)
        print (df)
    df = addSMA (df, 4)
    df = addSMA (df, 8)
    df = addSMA (df, 20)
    df = addSMA (df, 50)
    df = addExtensionSMA (df, 20)
    return df

### append moving average to df
def addSMA (df, sma):
    closeDf = df['close'].to_frame()
    name = 'sma' + str (sma)
    df [name] = closeDf['close'].rolling (sma).mean ()
    return df

def addExtensionSMA (df, sma):
    closeDf = df ['close'].to_frame()
    smaname = 'sma' + str (sma)
    sma20 = df [smaname].to_frame ()
    name = smaname + 'ext'
    df [name] =  (closeDf['close'] - sma20[smaname])/sma20[smaname]
    return df
