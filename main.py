import pandas as pd
from yFin import *
from constants import tickers, paths
from visualize import plotChart
from utils import writeDfToCsv, readDfFromCsv, formatDate

def buildCompleteDatasetBtc ():
    timeInterval = 'monthly'
    symbol = 'BTC-USD'
    filePath = '{}{}{}{}/'.format (paths['basePath'], paths['csvPath'], paths['cryptoPath'], timeInterval)
    filename = '{}-{}'.format(symbol, formatDate())
    r = readDfFromCsv (filePath + filename).drop (['adjclose'], axis = 1)
    h = readDfFromCsv ('data/historical-monthly').drop (['adjclose'], axis = 1)
    #h = h.iloc[::-1]
    df = pd.concat ([h, r])
    print (df)
    writeDfToCsv (df, path = 'data/', filename = 'complete')
    #plotChart (readDfFromCsv ('data/complete'))

buildCompleteDatasetBtc ()
