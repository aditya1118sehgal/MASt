import pandas as pd
from yFin import *
from constants import tickers, paths
from visualize import plotChart, plotChartSubplots
from utils import writeDfToCsv, readDfFromCsv, formatDate
from datasetBuilder import buildCompleteDatasetBtc, addExtensionSMA, addSMA

df =  buildCompleteDatasetBtc()
plotChartSubplots (df)
