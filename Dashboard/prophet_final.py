import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from prophet import Prophet
import plotly as plot
from matplotlib import pyplot
from prophet.plot import plot_plotly, plot_components_plotly

import plotly.graph_objs as go
import plotly.offline as py
from plotly.offline import init_notebook_mode
init_notebook_mode(connected=True)
import requests        
import json           
import pandas as pd    
import numpy as np     

import matplotlib.pyplot as plt 
import datetime as dt 

import streamlit as st

import pymongo
from pymongo import MongoClient

def get_bars(symbol, interval = '1m'):
    
    # Access API and reformat
    root_url = 'https://api.binance.com/api/v1/klines'
    url = root_url + '?symbol=' + symbol + '&interval=' + interval
    data = json.loads(requests.get(url).text)
    df = pd.DataFrame(data)
    df.columns = ['open_time',
                 'o', 'h', 'l', 'c', 'v',
                 'close_time', 'qav', 'num_trades',
                 'taker_base_vol', 'taker_quote_vol', 'ignore']
    df.index = [dt.datetime.fromtimestamp(x/1000.0) for x in df.close_time]
    df = df.reset_index()
    df = df.rename(columns={"index":"ds","open_time": "time", "o": "open", "h":"high", "l":"low", "c":"y", "v":"volume"})
    df_isolated = pd.DataFrame(df, columns = ['ds', 'y'])
    
    df_isolated.to_csv(r'coin_price_action.csv', mode = 'w', header = True, index=False)
    df1 = pd.read_csv("coin_price_action.csv")
    
    # Create prediction through Prophet model
    m = Prophet(changepoint_prior_scale=0.01, daily_seasonality=True).fit(df_isolated)
    future = m.make_future_dataframe(periods=30, freq='1min')
    fcst = m.predict(future)

    # Initialize PyMongo to work with MongoDBs
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    
    # Define database and collection
    # Name & create mongo database (i.e crypto_db)
    # Create variable for collection within mongo database 
    db = client.crypto_db
    collection = db.items
    
    #Reformat
    mongo_df = df.to_dict('records')
    
    # Delete all data from collection
    collection.remove({})

    #Load dictionary into mongo db
    collection.insert_many(mongo_df)

    # Create graph
    figure = plot_plotly(m, fcst)
    return figure 
    