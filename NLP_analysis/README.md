# NLP Analysis
This section deals with the natural language processing techniques used to read in cryptocurrency sentiment based on popular, relevant tweets scraped using the Twitter API. 

## Approach 
### Data & Data Preprocessing
- Tweets are scraped using the Tweepy Python library (connected to Twitter developer account).
    -   Filtered for most recent tweets with > 1000 favourites minimum.
- Tweets are organized into a Pandas Dataframe and cleaned using Regular Expression and tokenized using built-in nltk functions.

### Model
- Vader Sentiment library is used for sentiment analysis yielding a score between -1 (negative) to 1 (positive).
    -  See [test_files folder](https://github.com/findthefunction/goldendwarf/tree/main/NLP_analysis/test_files) for more info on the VADER library.
- Vader SentimentIntensityAnalyzer is used to create polarity scores for each tweet
    - Directed toward 'cleaned_text' column to maintain  the integrity of context, punctuation, etc. which is most beneficial for the vader library.
    - Tokenized columns used for wordcloud production.
    - Polarity scores are averaged to determine overall social sentiment score (between -1 and 1).

### Visualizations 
- A bar chart is outputted reflecting total number of tweets and average polarity scores for each sentiment category (ie positive, negative, neutral).
- Word cloud visualization is also outputted.

## Files 
- See [Twitter_NLP.ipynb](https://github.com/findthefunction/goldendwarf/blob/main/NLP_analysis/Twitter_NLP.ipynb) to see NLP process in full. 
- See [Twitter_NLP_Final.ipynb](https://github.com/findthefunction/goldendwarf/blob/main/NLP_analysis/Twitter_NLP_Final.ipynb) for condensed version of the code and wordcloud addition
  -  note: [Twitter_NLP_Final.py](https://github.com/findthefunction/goldendwarf/blob/main/Dashboard/Twitter_NLP_Final.py) is the final refactored code used to import into the dashboard.
- See [crypto_bar_graph.png](https://github.com/findthefunction/goldendwarf/blob/main/NLP_analysis/crypto_bar_graph.png) for a sample version of the outputted graph.
- See [output.png](https://github.com/findthefunction/goldendwarf/blob/main/NLP_analysis/output.png) for sample wordcloud image.
