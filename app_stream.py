from numpy import expand_dims
from numpy.core.numeric import _maketup
import streamlit as st
import Twitter_NLP_Final 
import prophet_remake as pp
import plotly.graph_objects as go
import pandas as pd
import requests        
import json  
import datetime as dt 
import pymongo
from pymongo import MongoClient

# Set ignore warning 
st.set_option('deprecation.showPyplotGlobalUse', False)


# Create titles for cryptocoin variables
ADA = "Cardano (ADA)"
BTC = "Bitcoin (BTC)"
ETH = "Etherium (ETH)"
DOT = "Polkadot (DOT)"
DOGE = "Dogecoin (DOGE)"
BNB = "Binance Coin (BNB)"


#Forecast and allow to collect cache for optimized performance
#@st.cache(allow_output_mutation=True)

def forecast(selection):

    if selection == ADA:
        coin = ('ADABUSD')
        title = "Cardano Price Action"

    if selection == BTC:
        coin = ('BTCBUSD')
        title = "Bitcoin Price Action"

    if selection == ETH:
        coin = ('ETHBUSD')
        title = "Etherium Price Action"

    if selection == DOT:
        coin = ('DOTBUSD')
        title = "Polkadot Price Action"

    if selection == DOGE:
        coin = ('DOGEBUSD')
        title = "Dogecoin Price Action"

    if selection == BNB:
        coin = ('BNBBUSD')
        title = "Binance Coin Price Action"

    fig = pp.get_bars(coin)
    
    fig.update_layout(
        title=title, yaxis_title = "Price", xaxis_title="Date",
        )

    return fig


# Get database for cryptocurrency
def get_df(symbol, interval = '1m'):

    # Initialize PyMongo to work with MongoDBs
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    
    #select database
    db = client['crypto_db']
    #select the collection within the database
    df_data = db.items
    
    #convert entire collection to Pandas dataframe
    df = pd.DataFrame(list(df_data.find()))
    df = df.drop(columns = ['open_time','o', 'h', 'l', 'c', 'v', 'index', 'ignore', '_id', 'time'])

    return df


def dfdata(selection):

    if selection == ADA:
        coin = ('ADABUSD')
        title = "Cardano Price Action"

    if selection == BTC:
        coin = ('BTCBUSD')
        title = "Bitcoin Price Action"

    if selection == ETH:
        coin = ('ETHBUSD')
        title = "Etherium Price Action"

    if selection == DOT:
        coin = ('DOTBUSD')
        title = "Polkadot Price Action"

    if selection == DOGE:
        coin = ('DOGEBUSD')
        title = "Dogecoin Price Action"

    if selection == BNB:
        coin = ('BNBBUSD')
        title = "Binance Coin Price Action"

    dataf = get_df(coin)

    return dataf

# Create Sidebar 
menu = ['Price Forecast', 'Twitter Sentiment']

choice = st.sidebar.selectbox("Menu", menu)

if choice == 'Price Forecast':
    
    # Create dropdown-menu / interactive forecast graph
    st.write("# Cryptocurrency and Machine Learning")
    
    about_bar = st.beta_expander("About This Section:")

    about_bar.markdown("""
    * The interactive chart below combines both the price action of the cryptocurrency and a 30-minute forecast at the tail of the chart. 
    * This forecast is powered by the incredible python library "fbprophet" developed by Facebook.  
    """)

    st.write("## Cryptocurrency 30-minute Forecast")
    

    select_series = st.selectbox("Select a coin:", (BTC, ETH, DOGE, ADA, DOT, BNB))
    
    forecast_graph = forecast(select_series)
    st.plotly_chart(forecast_graph)
    

    st.write("## Database powering the graph above")
    df = dfdata(select_series)
    st.dataframe(df)



elif choice == 'Twitter Sentiment':

    st.write("# Cryptocurrency and Machine Learning")

    about_bar2 = st.beta_expander("About This Section:")

    about_bar2.markdown("""
    * The images below represent our NLP analysis on recent Twitter data in the following ways:
        - Bar chart representing the number of positive, negative and neutral tweets with average polarity scores for each sentiment. 
        - Average overall sentiment score in the market based on tweets.
        - A word cloud image containing token words from the analysis.
    """)
    
    st.write("## Market Sentiment and NLP")
    
    # Set columns
    #col1, col2 = st.beta_columns((9,1))
    
    # Plotly Graph
    bar_graph = Twitter_NLP_Final.plotly_graph()
    #with col2:
    show_bar = st.plotly_chart(bar_graph)
        
    # Average Sentiment Score
    gauge_chart = go.Figure(go.Indicator(
        mode='gauge+number+delta', 
        value = Twitter_NLP_Final.scrape_sentiment_score(),
        title = {'text': 'Average Sentiment Score (-1.0 Negative to 1.0 Positive)'}, 
        gauge = {
            'axis': {'range': [-1, 1]},
            'bar': {'color':'lightgrey'}, 
            'steps': [
                {'range': [-1, -0.75], 'color': 'rgb(255, 84, 84)'}, 
                {'range': [-0.75, -0.25], 'color': 'rgb(255,141,84)'}, 
                {'range': [-0.25, 0.25], 'color': 'rgb(255,250,84)'},
                {'range': [0.25, 0.75], 'color': 'rgb(216,255,84)'}, 
                {'range': [0.75, 1], 'color': 'rgb(130,255,84)'}
            ]
            }
        ))
    
    #with col1:
    show_gauge = st.plotly_chart(gauge_chart)
    
    # Show wordcloud image
    
    Twitter_NLP_Final.wrrrdcloud()





