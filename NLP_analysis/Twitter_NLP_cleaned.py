## Twitter Scraping & NLP

import requests 
import json
from config import consumer_key, consumer_secret, access_key, access_secret, bearer_token

import pandas as pd
import sys
import tweepy
import matplotlib.pyplot as plt
import numpy as np
import os
import seaborn as sns
import time
import re
import string

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer 
from nltk.corpus import wordnet
nltk.download('averaged_perceptron_tagger')
nltk.download('vader_lexicon')
nltk.download('stopwords')
nltk.download('wordnet')

get_ipython().system('pip install gensim')
import gensim
from gensim.parsing.preprocessing import remove_stopwords 

from wordcloud import WordCloud, STOPWORDS
from PIL import Image
from langdetect import detect
from sklearn.feature_extraction.text import CountVectorizer

# Display max column width 
pd.set_option('display.max_colwidth', None)


## Twitter API (Tweepy)

# Initialize and gain access to Twitter API
def initialize():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return api

api = initialize()


# Scraping function
def twitter_scrape():
    
    search_words = ("bitcoin", "etherium", "cardano")
    crypto_data = pd.DataFrame()
    
    def get_data(data):
        data = {
            'text': data.full_text,
            'date': data.created_at,
            'followers': data.user.followers_count,
            'favourites': data.user.favourites_count,
            'retweets': data.retweet_count
        }
        return data
    
    for tweets in search_words:
        comp_tweets = api.search(q=tweets, lang = 'en', result_type = 'recent', count=250, tweet_mode='extended')
        
        for tweet in comp_tweets:
            row = get_data(tweet)
            crypto_data = crypto_data.append(row, ignore_index=True)
    
    
    # Formatting
    # Keep only tweets with over 1000 favourites
    crypto_data = crypto_data.loc[crypto_data['favourites']>1000]
    
    # Clean text column using Regex
    crypto_data['cleaned_text'] = crypto_data['text']
    clean_text = '(RT) @[\w]*:|(@[A-Za-z0-9]+)|([^\,\!\.\'\%0-9A-Za-z \t])|(\w+:\/\/\S+)'
    crypto_data['cleaned_text'] = crypto_data['cleaned_text'].str.replace(clean_text, " ", regex=True)
    crypto_data['cleaned_text'] = crypto_data['cleaned_text'].str.lower()
        
    # Convert date dtype to datetime, set index, sort index and drop duplicates
    crypto_data['date'] = pd.to_datetime(crypto_data['date'])
    crypto_data = crypto_data.set_index('date').sort_index(ascending=False)
    crypto_data.drop_duplicates(inplace=True)
    
    
    #Tokenizing
    # Tokenizing Functions
    def get_wordnet_pos(word):
        # Map POS tag to the first character lemmatize() accepts
        tag = nltk.pos_tag([word])[0][1][0].upper()
        tag_dict = {"J": wordnet.ADJ,
                    "N": wordnet.NOUN,
                    "V": wordnet.VERB,
                    "R": wordnet.ADV}
        
        return tag_dict.get(tag, wordnet.NOUN)
    
    # Function for tokenizing tweets (already cleaned using regex)
    def second_clean(tweet):
        tweet = remove_stopwords(tweet) # remove stopwords with Gensim
        
        lemmatizer = WordNetLemmatizer()
        tokenized = [lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in nltk.word_tokenize(tweet)]
        
        # remove left over stop words with nltk
        tokenized = [token for token in tokenized if token not in stopwords.words("english")] 
        
        # remove non-alpha characters and keep the words of length >2 only
        tokenized = [token for token in tokenized if token.isalpha() and len(token)>2]
        
        return tokenized
    
    # Function for joining tokenized list into string
    def combine_tokens(tokenized): 
        non_tokenized = ' '.join([w for w in tokenized])
        return non_tokenized
    
    # Execute token functions
    crypto_data['tokens'] = crypto_data['cleaned_text'].apply(lambda x: second_clean(x))
    crypto_data['final_clean'] = crypto_data['tokens'].apply(lambda x: combine_tokens(x))

    
    # NLP - Vader Sentiment Model 
    # Sentiment labels function 
    
    sia = SentimentIntensityAnalyzer()
    
    def sentiment_labels(df, feature, value): 
        df.loc[df[value] > 0,feature] = 'positive'
        df.loc[df[value] == 0,feature] = 'neutral'
        df.loc[df[value] < 0,feature] = 'negative'
    
    def vader_sentiment(df):
        target_col='cleaned_text'
        prefix = 'vader_clean_'
        
        scores_col=prefix+'scores'
        compound_col = prefix+'polarity'
        sentiment = prefix+'sentiment'
        
        df[scores_col] = df[target_col].apply(lambda x:sia.polarity_scores(x))
        df[compound_col] = df[scores_col].apply(lambda d: d['compound'])
        sentiment_labels(df, sentiment, compound_col)
    
    # Execute Vader Function
    vader_sentiment(crypto_data)
    
    
    # Get sentiment score 
    vader_values = crypto_data.loc[:, 'vader_clean_polarity']
    sentiment_score = round(np.mean(vader_values), 4)
    
    return sentiment_score