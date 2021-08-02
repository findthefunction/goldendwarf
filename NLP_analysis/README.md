# NLP Analysis
This section deals with the natural language processing techniques used to read in cryptocurrency sentiment based on popular, recent tweets from twitter. 

## Approach 
- Tweets are scraped using the Twitter API and executed through the tweepy module.
- Vader Sentiment library is used for sentiment analysis yielding a score between -1 (negative) to 1 (positive).
    -  See [test_files folder](https://github.com/findthefunction/goldendwarf/tree/andrew/NLP_analysis/test_files) for more info on the VADER library
- Tweets are cleaned using Regular Expression and tokenized with built-in nltk functions 
- To determine sentimeNt score, the vader SentimentIntensityAnalyzer is directed toward the partially cleaned tweets column (ie 'cleaned_text') to keep the integrity of context, punctuation, etc which is beneficial to the vader model. 
- A bar chart is outputted reflecting total number of tweets and average polarity scores for each sentiment category (ie positive, negative, neutral). 
- Word cloud visualization is also outputted

# Files 
- See [Twitter_NLP.ipynb](https://github.com/findthefunction/goldendwarf/blob/andrew/NLP_analysis/Twitter_NLP.ipynb) to see NLP process in full. 
- See [Twitter_NLP_Final.ipynb](https://github.com/findthefunction/goldendwarf/blob/andrew/NLP_analysis/Twitter_NLP_Final.ipynb) for condensed version of the code.
  -  note: [Twitter_NLP_Final.py](https://github.com/findthefunction/goldendwarf/blob/andrew/NLP_analysis/Twitter_NLP_Final.py) is the final refactored code used to import into the dashboard.
- See [crypto_bar_graph.png](https://github.com/findthefunction/goldendwarf/blob/andrew/NLP_analysis/crypto_bar_graph.png) for a sample version of the outputted graph.
- See [output.png](https://github.com/findthefunction/goldendwarf/blob/andrew/NLP_analysis/output.png) for sample wordcloud image.
