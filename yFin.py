from yahoofinancials import YahooFinancials
from utils import getEndDate
import pandas as pd

YF_BTC_START = '2014-09-15'

def pullTickerData (ticker, startDate = YF_BTC_START, endDate = getEndDate(), timeInterval='weekly'):
    yahoo_financials = YahooFinancials(ticker)
    data = yahoo_financials.get_historical_price_data(start_date=startDate,
                                                      end_date=endDate,
                                                      time_interval='weekly')
    df = pd.DataFrame(data[ticker]['prices'])
    df = df.drop('date', axis=1).set_index('formatted_date')
    return df


def pullCryptoData (symbol='BTC-USD', startDate = YF_BTC_START, endDate = getEndDate(), timeInterval='weekly'):
    yahoo_financials = YahooFinancials(symbol)
    data=yahoo_financials.get_historical_price_data (
            start_date = startDate,
            end_date = endDate,
            time_interval=timeInterval
        )
    btc_df = pd.DataFrame(data[symbol]['prices'])
    btc_df = btc_df.drop('date', axis=1).set_index('formatted_date')
    return btc_df

# test
#print (getCryptoData ())
