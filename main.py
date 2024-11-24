import pandas as pd
from sguppy import guppy
from yFin import *
from constants import tickers, paths
from visualize import *
from utils import writeDfToCsv, readDfFromCsv, formatDate
from datasetBuilder import buildCompleteDatasetBtc, addExtensionSMA, addSMA

def main ():
    df =  pullCryptoData ()
    print (df)
    df = guppy (df)
    print (df)

    #plotChartSubplots (df)

    df.to_csv ('sg.csv')
    plotGuppy (df)

if __name__ == "__main__":
    main()
