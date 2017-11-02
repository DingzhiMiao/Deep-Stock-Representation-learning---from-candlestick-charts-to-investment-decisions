import datetime as dt
from pandas_datareader import data, wb
import os
import fix_yahoo_finance as yf
import time
# fixed pandas_datareader can't download from yahoo finance
yf.pdr_override()

stock_list = ['^FTSE']


def fetch_yahoo_data(ticker, start_date, end_date, fname, max_attempt, check_exist=True):
    if (os.path.exists(fname) == True) and check_exist:
        print("file exist")
    else:
        for attempt in range(max_attempt):
            time.sleep(2)
            try:
                dat = data.DataReader(''.join("{}".format(
                    ticker)), 'yahoo', start_date, end_date)
                dat.to_csv(fname)
            except Exception as e:
                if attempt < max_attempt - 1:
                    print('Attempt {}: {}'.format(attempt + 1, str(e)))
                else:
                    raise
            else:
                break


# fetch all data
for ticker in set(stock_list):
    fetch_yahoo_data(ticker, "2000-01-04", "2017-05-14","{}.csv".format(ticker), 10)
