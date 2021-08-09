# Project Goldendwarf
Utilizing machine learning and natural language processing techniques to predict future price movements of cryptocurrencies (and stocks) as well as gauging social sentiment of the crypto universe.

## Purpose
- Applying neural network fundamentals & data analytics knowledge to forecast price action in the cryptocurrency space. 
- Outputs from analysis would collectively help determine potetial market risk in the buying/selling of cryptocurrency assets. 
- Looks to the future would be directed toward using this collective analysis to feed a real-time automated machine that generates alpha through trading cryptocurrency.

### Questions to Answer 
- Can the model accurately predict price movement more than 50% of the time? (Is it better than flipping a coin?)
- Can the contributive analysis be successful in feeding information to a well-operating trading bot (for future development)?
    -  Can the code be optimized sufficiently to be real-time operational (or close to it)?
    -  Is our implementation strategy scaleable?

## Analysis 
### Components
- Machine Learning (See the [neural_network folder](https://github.com/findthefunction/goldendwarf/tree/main/neural_network) for further description & code): 
    - FB Prophet: Using Facebook's FBProphet machine learning library to forecast crypto price-movement in real-time.
    - Bi-Directional RNN: Training our own bi-directional recurrent neural network for greater improvements in predictive accuracy (currently in production).
    
- Natural Language Processing (See the [NLP_analysis folder](https://github.com/findthefunction/goldendwarf/tree/main/NLP_analysis) and [NLP Wordcloud folder](https://github.com/findthefunction/goldendwarf/tree/main/NLP%20Wordcloud) for further description & code):
    - Scraping and analyzing relevant twitter data to develop a cryptocurrency social sentiment score in real-time.

### Data & Data Storage 
- Data scraped using the following APIs:
    -  Binanace API 
    -  Tweepy Library (Twitter API)
- Database 
    - MongoDB for data storage (for future referencing and retrieving relevant tables for the interactive dashboard).
    - Data is updated every time a new coin is selected.

*See sample price-action data stored in MongoDB below (visualized as dataframes using Streamlit)*

<img width="697" alt="Screen Shot 2021-08-08 at 6 06 22 PM" src="https://user-images.githubusercontent.com/79600550/128647113-6a8514d8-6fbe-4a0d-9341-911b9e4af6cd.png">

<img width="699" alt="Screen Shot 2021-08-08 at 6 06 36 PM" src="https://user-images.githubusercontent.com/79600550/128647115-37def003-75c0-4557-8bb2-656caacc0f86.png">


## Dashboard 
- Check out our [Demo Video](https://www.youtube.com/watch?v=7wdJV34Jdxc&t=2s) to see how the interactive dashboard operates. 
- Created using Streamlit and Plotly, the interactive dashboard displays price forecasting of selected coins and social sentiment scores of the cryptocurrency market in real-time.
- Code can be referenced in the [Dashboard folder](https://github.com/findthefunction/goldendwarf/tree/main/Dashboard).

<img width="639" alt="Screen Shot 2021-08-09 at 2 10 12 PM" src="https://user-images.githubusercontent.com/79600550/128753361-6a9f8127-637f-45e7-93a8-8b136e7d2f55.png">

## Google Slides
- Follow this [link](https://docs.google.com/presentation/d/124W2VgxM6cSDz5dqoKisK2hXoikAnP9mSJqux85g4EY/edit?usp=sharing) to see our presentation slides. 
