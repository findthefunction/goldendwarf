# Project Goldendwarf
Utilizing machine learning and natural language processing techniques to predict future price movements of cryptocurrencies (and stocks) as well as gauging social sentiment of the crypto universe.

## Purpose
- Applying neural network fundamentals & data analytics knowledge to forecast price action in the cryptocurrency space. 
- Outputs from analysis would collectively help determine potetial market risk in the buying/selling of cryptocurrency assets. Looks to the future would be directed toward using this collective analysis to feed a real-time automated machine that generates alpha through trading cryptocurrency.

### Questions to Answer 
- Can the model accurately predict price movement more than 50% of the time? (Is it better than flipping coin?)
- Can the contributive analysis be successful in feeding information to a well-operating trading bot (in future development)?
    -  Can the code be optimized sufficiently to be real-time operational (or close to it)?
    -  Is our implementation strategy scaleable?

## Analysis 
### Components
- Machine Learning (See the [neural_network folder](https://github.com/findthefunction/goldendwarf/tree/main/neural_network) for code): 
    - FB Prophet: Using the Facebook's FBProphet machine learning library to forecast crypto price movement real-time.
    - Bi-Directional RNN: Training our own bi-directional recurrent neural network for even greater improvements in accuracy (currently in production).
    
- Natural Language Processing (See the [NLP_analysis folder](https://github.com/findthefunction/goldendwarf/tree/main/NLP_analysis) and [NLP Wordcloud folder](https://github.com/findthefunction/goldendwarf/tree/main/NLP%20Wordcloud) for code):
    - Scraping and analyzing relevant twitter data to develop a cryptocurrency social sentiment score in real-time.

### Data & Data Storage 
- Data scraped using the following APIs:
    -  Binanace API 
    -  Tweepy Library (Twitter API)
- Database 
    - MongoDB for data storage (for future referencing and retrieving relevant tables for the interactive dashboard) 

## Dashboard 
- Check out our [Demo Video](https://www.youtube.com/watch?v=7wdJV34Jdxc&t=2s) to see how the interactive dashboard operates. 
- Created using Streamlit and Plotly, the interactive dashboard displays price forecasting of selected coins and social sentiment scores of the cryptocurrency market in real-time.
- Code can be referenced in the [Dashboard folder](https://github.com/findthefunction/goldendwarf/tree/main/Dashboard).

## Google Slides
- Follow this [link](https://docs.google.com/presentation/d/124W2VgxM6cSDz5dqoKisK2hXoikAnP9mSJqux85g4EY/edit?usp=sharing) to see our presentation slides. 
