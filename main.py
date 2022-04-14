'''
from yFin import *
from constants import tickers, paths
from visualize import plotChart
from utils import writeDfToCsv, readDfFromCsv, formatDate

timeInterval = 'weekly'
symbol = 'BTC-USD'
#c = pullCryptoData (symbol = symbol, timeInterval = timeInterval)
#print (c)
filePath = '{}{}{}{}/'.format (paths['basePath'], paths['csvPath'], paths['cryptoPath'], timeInterval)
filename = '{}-{}'.format(symbol, formatDate())
#writeDfToCsv (df = c, path = filePath,filename = filename)
r = readDfFromCsv (filePath + filename)
print (r)
plotChart (r)
'''
