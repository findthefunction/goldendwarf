# NLP Analysis
This section deals with the natural language processing techniques used to read in cryptocurrency sentiment based on popular, relevant tweets scraped using the Twitter API. 

## Approach 
### Data & Data Preprocessing
Tweets are scraped using the Tweepy Python library and organized into a Pandas Dataframe. Data is filtered for most recent tweets with over 1000 favourites minimum to help ensure relevance and influence of the tweets at hand. Tweets are then tokenized using built-in nltk functions.


### Model - Vader Sentiment Library
The Vader library's SentimentIntensityAnalyzer is used to create sentiment scores for each tweet, combining the scores of each sentiment (pos, neg, neu) to form a single compound score ranging between -1 and 1 (See [test_files folder](https://github.com/findthefunction/goldendwarf/tree/main/NLP_analysis/test_files) for more info on the Vader Sentiment Library). These polarity scores are then averaged to form an overall twitter cryptocurrency sentiment score. The SentimentIntensityAnalyzer is specifically directed at the 'clean_text' column - a partially cleaned column using only RegEx - in order to maintain the integrity of context, punctuation use, etc. which is beneficial to the vader library's analysis. Tokenized columns are only used for wordcloud production in this case.

- Benefits
    - The Vader Sentiment library is specifically engineered for social media/microblog contexts.
    - The library holds an extensive array of built in heuristics to recognize many syntactical elements relevant in tweet-like contexts:
        - word negations, intensifiers, punctuation, word-shape, degree modifiers, initialisms, acronyms, etc
        - strong tolerance for micro-blog-type slang and utf-8 encoded emoji recognition   
- Cons 
    - The model can't always recognize typos and will analyze such words as out-of-vocabulary words.
    - Vader is a pre-trained model and therefore is less malleable than creating a custom machine learning model. A custom model, however, would require a subjective classification of tweets that the model would need to be trained on, and therefore could be extremely susceptible to overfitting. Furthermore, it would lack many of the complexities several of the popular sentiment models already contain, which are used extensively to determine sentiment in contexts such as twitter. This is, however, still most definitely a look toward future analysis.

### Visualizations 
A bar chart is outputted reflecting total number of tweets and average polarity scores for each sentiment category (ie positive, negative, neutral). A Word cloud visualization is also outputted.

## Files 
- See [Twitter_NLP.ipynb](https://github.com/findthefunction/goldendwarf/blob/main/NLP_analysis/Twitter_NLP.ipynb) to see NLP process in full. 
- See [Twitter_NLP_Final.ipynb](https://github.com/findthefunction/goldendwarf/blob/main/NLP_analysis/Twitter_NLP_Final.ipynb) for condensed version of the code and wordcloud addition
  -  note: [Twitter_NLP_Final.py](https://github.com/findthefunction/goldendwarf/blob/main/Dashboard/Twitter_NLP_Final.py) is the final refactored code used to import into the dashboard.
- See [crypto_bar_graph.png](https://github.com/findthefunction/goldendwarf/blob/main/NLP_analysis/crypto_bar_graph.png) for a sample version of the outputted graph.
- See [output.png](https://github.com/findthefunction/goldendwarf/blob/main/NLP_analysis/output.png) for sample wordcloud image.
