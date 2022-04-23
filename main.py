import pandas as pd
from yFin import *
from constants import tickers, paths
from visualize import plotChart
from utils import writeDfToCsv, readDfFromCsv, formatDate
from datasetBuilder import buildCompleteDatasetBtc, addExtensionSMA, addSMA

df =  buildCompleteDatasetBtc()
df = addSMA (df, 20)
df = addExtensionSMA (df, 20)
#writeDfToCsv (df, path = 'data/', filename = 'complete')
plotChart (df)
