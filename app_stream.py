from numpy.core.numeric import _maketup
import streamlit as st
import Twitter_NLP_Final 
import prophet_remake as pp
import plotly.graph_objects as go




# Set ignore warning 
st.set_option('deprecation.showPyplotGlobalUse', False)


# Create titles for cryptocoin variables
ADA = "Cardano (ADA)"
BTC = "Bitcoin (BTC)"
ETH = "Etherium (ETH)"
DOT = "Polkadot (DOT)"
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

    if selection == BNB:
        coin = ('BNBUSD')
        title = "Binance Coin Price Action"

    fig = pp.get_bars(coin)
    
    fig.update_layout(
        title=title, yaxis_title = "Price", xaxis_title="Date",
        )

    return fig

# Create Sidebar 
menu = ['Price Forecast', 'Twitter Sentiment']

choice = st.sidebar.selectbox("Menu", menu)

if choice == 'Price Forecast':
    
    # Create dropdown-menu / interactive forecast graph
    st.write("# Cryptocurrency and Machine Learning")
    
    st.write("## Cryptocurrency 30-minute Forecast")
    

    select_series = st.selectbox("Select a coin:", (ADA, BTC, ETH, DOT, BNB))
    
    forecast_graph = forecast(select_series)
    st.plotly_chart(forecast_graph)

elif choice == 'Twitter Sentiment':

    st.write("# Cryptocurrency and Machine Learning")
    
    st.write("## Market Sentiment")
    
    # Set columns
    col1, col2 = st.beta_columns([4,1])
    
    # Plotly Graph
    bar_graph = Twitter_NLP_Final.plotly_graph()
    with col1:
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
    
    with col2:
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





