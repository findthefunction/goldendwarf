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

#st.set_page_config(layout="wide")

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
@st.cache(allow_output_mutation=True)

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
    #df_isolated = pd.DataFrame(df, columns = ['ds', 'y'])
    
    #df_isolated.to_csv(r'coin_price_action.csv', mode = 'w', header = True, index=False)
    #df1 = pd.read_csv("coin_price_action.csv")
    
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
    
    st.write("## Market Sentiment")
    
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


# #Test 

# base_chart = {
#     "values": [40, 10, 10, 10, 10, 10, 10],
#     "labels": ["-", "-1", "-0.75", "-0.25", "0.25", "0.75", "1"],
#     "domain": {"x": [0, .48]},
#     "marker": {
#         "colors": [
#             'rgb(255, 255, 255)',
#             'rgb(255, 255, 255)',
#             'rgb(255, 255, 255)',
#             'rgb(255, 255, 255)',
#             'rgb(255, 255, 255)',
#             'rgb(255, 255, 255)',
#             'rgb(255, 255, 255)'
#         ],
#         "line": {
#             "width": 1
#         }
#     },
#     "name": "Gauge",
#     "hole": .4,
#     "type": "pie",
#     "direction": "clockwise",
#     "rotation": 108,
#     "showlegend": False,
#     "hoverinfo": "none",
#     "textinfo": "label",
#     "textposition": "outside"
# }

# meter_chart = {
#     "values": [50, 10, 10, 10, 10, 10],
#     "labels": ["Twitter Sentiment", "Negative", "", "Neutral", "", "Positive"],
#     "marker": {
#         'colors': [
#             'rgb(255, 255, 255)',
#             'rgb(255, 84, 84)',
#             'rgb(255,141,84)',
#             'rgb(255,250,84)',
#             'rgb(216,255,84)',
#             'rgb(130,255,84)'
#         ]
#     },
#     "domain": {"x": [0, 0.48]},
#     "name": "Gauge",
#     "hole": .3,
#     "type": "pie",
#     "direction": "clockwise",
#     "rotation": 90,
#     "showlegend": False,
#     "textinfo": "label",
#     "textposition": "inside",
#     "hoverinfo": "none"
# }

# layout = {
#     'xaxis': {
#         'showticklabels': False,
#         'showgrid': False,
#         'zeroline': False,
#     },
#     'yaxis': {
#         'showticklabels': False,
#         'showgrid': False,
#         'zeroline': False,
#     },
#     'shapes': [
#         {
#             'type': 'path',
#             'path': 'M 0.235 0.5 L 0.24 0.65 L 0.245 0.5 Z',
#             'fillcolor': 'rgba(44, 160, 101, 0.5)',
#             'line': {
#                 'width': 0.75
#             },
#             'xref': 'paper',
#             'yref': 'paper'
#         }
#     ],
#     'annotations': [
#         {
#             'xref': 'paper',
#             'yref': 'paper',
#             'x': 0.23,
#             'y': 0.45,
#             'text': '100',
#             'showarrow': False
#         }
#     ]
# }

# # we don't want the boundary now
# base_chart['marker']['line']['width'] = 0

# gauge2 = {"data": [base_chart, meter_chart],
#        "layout": layout}

# st.plotly_chart(gauge2)

# #py.iplot(fig, filename='gauge-meter-chart')


# # Average Sentiment Score
# gauge_chart = go.Figure(go.Indicator(
#     mode='gauge+number+delta', 
#     value = Twitter_NLP_Final.scrape_sentiment_score(),
#     title = {'text': 'Twitter Sentiment (-1.0 Negative to 1.0 Positive)'}, 
#     gauge = {
#         'axis': {'range': [-1, 1]},
#         'bar': {'color':'lightgrey'}, 
#         'steps': [
#             {'range': [-1, -0.75], 'color': 'rgb(255, 84, 84)'}, 
#             {'range': [-0.75, -0.25], 'color': 'rgb(255,141,84)'}, 
#             {'range': [-0.25, 0.25], 'color': 'rgb(255,250,84)'},
#             {'range': [0.25, 0.75], 'color': 'rgb(216,255,84)'}, 
#             {'range': [0.75, 1], 'color': 'rgb(130,255,84)'}
#             ]
#             }
#         ))

# st.plotly_chart(gauge_chart)





