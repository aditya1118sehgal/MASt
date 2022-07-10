import pandas as pd
from yFin import *
from constants import tickers, paths
from visualize import plotChart
from utils import writeDfToCsv, readDfFromCsv, formatDate
from pathlib import Path

SYMBOL = 'BTC-USD'
def buildCompleteDatasetBtc (filename = '{}-{}'.format(SYMBOL, formatDate())):
    timeInterval = 'monthly'
    filePath = '{}{}{}{}/{}/'.format (paths['basePath'], paths['csvPath'], paths['cryptoPath'], SYMBOL, timeInterval)
    df = None
    print (filePath + filename+'.csv')
    if not Path(filePath + filename+'.csv').is_file():
        print ('no file => pull data')
        r = pullCryptoData ()
        writeDfToCsv (r , filePath, filename)
        r = readDfFromCsv (filePath + filename)
        h = readDfFromCsv ('data/historical-monthly')
        df = pd.concat ([h, r])
        #df = addSMA (df, 4)
        #df = addSMA (df, 8)
        df = addSMA (df, 20)
        df = addEMA (df, 21)
        df = addSMA (df, 36)
        df = addSMA (df, 60)
        #df = addExtensionSMA (df, 20)
        sma20 = df ['sma20']
        ema21 = df ['ema21']
        deltaSma20 = df ['sma20'].diff()
        deltaEma21 = df ['ema21'].diff ()
        deltaSma36 = df ['sma36'].diff ()
        deltaSma60 = df ['sma60'].diff ()
        df ['deltaSma20'] = deltaSma20
        df ['deltaEma21'] = deltaEma21
        df ['deltaSma36'] = deltaSma36
        df ['deltaSma60'] = deltaSma60
        df ['slopeSma20'] = df ['deltaSma20']/df['sma20']
        df ['slopeEma21'] = df ['deltaEma21']/df ['ema21']
        df ['slopeSma36'] = df ['deltaSma36']/df ['sma36']
        df ['slopeSma60'] = df ['deltaSma60']/df ['sma60']
        writeDfToCsv (df, filePath, filename)
    else:
        print ('read file')
        df = readDfFromCsv (filePath + filename)
    return df

### append moving average to df
def addSMA (df, sma):
    closeDf = df['close'].to_frame()
    name = 'sma' + str (sma)
    df [name] = closeDf['close'].rolling (sma).mean ()
    return df

def addEMA (df, ema):
    closeDf = df['close'].to_frame()
    name = 'ema' + str (ema)
    df[name] = closeDf['close'].ewm(span = ema, adjust = False).mean()
    return df

def addExtensionSMA (df, sma):
    closeDf = df ['high'].to_frame()
    smaname = 'sma' + str (sma)
    sma20 = df [smaname].to_frame ()
    name = smaname + 'ext'
    df [name] =  (closeDf['high'] - sma20[smaname])/sma20[smaname]
    return df
