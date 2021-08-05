
import pandas as pd
import requests        
import json           
import numpy as np     

import matplotlib.pyplot as plt 
import datetime as dt 

def get_bars(symbol, interval = '1m'):
   root_url = 'https://api.binance.com/api/v1/klines'
   url = root_url + '?symbol=' + symbol + '&interval=' + interval
   data = json.loads(requests.get(url).text)
   df = pd.DataFrame(data)
   df.columns = ['open_time',
                 'o', 'h', 'l', 'c', 'v',
                 'close_time', 'qav', 'num_trades',
                 'taker_base_vol', 'taker_quote_vol', 'ignore']
   df.index = [dt.datetime.fromtimestamp(x/1000.0) for x in df.close_time]
   return df

#ADA

adabusd = get_bars('ADABUSD')

adabusd.to_csv(r'data/ada_busd.csv', mode = 'a', header = True)

ada_df = pd.read_csv (r'data/ada_busd.csv')

ada_df = ada_df.drop(ada_df.columns[[0,7,8,9,10,11,12]], axis=1)
#df = df.drop(df.columns[[0, 1, 3]], axis=1)
ada_df=ada_df.rename(columns={"open_time": "time", "o": "open", "h":"high", "l":"low", "c":"close", "v":"volume"})
ada_df.head()
#ada_df.to_json(r'data/ada_rnn.json', mode = 'a', header = False, index=False)
#ada_df.to_json(r'data/ada_rnn.json', orient = 'records', lines=True)

#ETH

ethbusd = get_bars('ETHBUSD')

ethbusd.to_csv(r'data/eth_busd.csv', mode = 'a', header = True)

eth_df = pd.read_csv (r'data/eth_busd.csv')

eth_df = eth_df.drop(eth_df.columns[[0,7,8,9,10,11,12]], axis=1)
#df = df.drop(df.columns[[0, 1, 3]], axis=1)
eth_df=eth_df.rename(columns={"open_time": "time", "o": "open", "h":"high", "l":"low", "c":"close", "v":"volume"})
eth_df.head()

#eth_df.to_json(r'data/eth_rnn.json', mode = 'a', header = False, index=False)
#eth_df.to_json(r'data/eth_rnn.json', orient = 'records', lines=True)

#BTC

btcbusd = get_bars('BTCBUSD')

#btcbusd.to_csv(r'data/btc_busd.csv', mode = 'a', header = True)
btcbusd.to_csv(r'data/btc_busd.csv', mode = 'a', header = True)

btc_df = pd.read_csv (r'data/btc_busd.csv')

btc_df = btc_df.drop(btc_df.columns[[0,7,8,9,10,11,12]], axis=1)
#df = df.drop(df.columns[[0, 1, 3]], axis=1)
btc_df=btc_df.rename(columns={"open_time": "time", "o": "open", "h":"high", "l":"low", "c":"close", "v":"volume"})
btc_df.head()

#btc_df.to_json(r'data/btc_rnn.json', mode = 'a', header = False, index=False)
#btc_df.to_json(r'data/btc_rnn.json', orient = 'records', lines=True)

#DOT

dotbusd = get_bars('DOTBUSD')

dotbusd.to_csv(r'data/dot_busd.csv', mode = 'a', header = True)

dot_df = pd.read_csv (r'data/dot_busd.csv')

dot_df = dot_df.drop(dot_df.columns[[0,7,8,9,10,11,12]], axis=1)
#df = df.drop(df.columns[[0, 1, 3]], axis=1)
dot_df=dot_df.rename(columns={"open_time": "time", "o": "open", "h":"high", "l":"low", "c":"close", "v":"volume"})
dot_df.head()

#dot_df.to_json(r'data/dot_rnn.json', mode = 'a', header = False, index=False)
#dot_df.to_json(r'data/dot_rnn.json', orient = 'records', lines=True)

df = pd.concat([ada_df, eth_df, btc_df, dot_df])

# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define database and collection
# Name & create mongo database (i.e crypto_db in this case)
# Create variable for collection within your mongo database 
db = client.crypto_data
collection = db.complete

# Load raw JSON BTC info data into mongo db
collection.insert_many(df.to_dict('records'))

