#!/usr/bin/env 
# coding: utf-8

# Raw Package
import numpy as np
import pandas as pd
import datetime as dt

#Data Source
import yfinance as yf

data = yf.download(  # or pdr.get_data_yahoo(...
        # tickers list or string as well
        tickers = "ADA-USD",

        # use "period" instead of start/end
        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        # (optional, default is '1mo')
        period = "1d",

        # fetch data by interval (including intraday if period < 60 days)
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        # (optional, default is '1d')
        interval = "1m",

        # group by ticker (to access via data['SPY'])
        # (optional, default is 'column')
        group_by = 'ticker',

        # use threads for mass downloading? (True/False/Integer)
        # (optional, default is True)
        threads = True,

        # proxy URL scheme use use when downloading?
        # (optional, default is None)
        proxy = None
    )


# Convert data to pd.DataFrame, fill NaN values with previous value, drop duplicates to remove overlaps

ada_data_df = pd.DataFrame(data).fillna(method = "backfill").drop_duplicates(keep = "first")


# ada_data_df.dtypes

# Convert to datetime
# ada_data_df['Datetime'] = pd.to_datetime(ada_data_df['Datetime'])
# # Remove timezone data from Datetime column
# ada_data_df['Datetime'] = ada_data_df['Datetime'].dt.tz_convert(None)


ada_data_df.to_csv(r'data/large_ada_data.csv', mode = 'a', header=False)






