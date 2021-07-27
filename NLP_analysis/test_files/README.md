# Testing NLP 

The above files are test pieces of code analyzing different strategies for NLP using the bitcoin mock dataset above (Cleaned_Bitcoin_tweets.csv). As this dataset is very similar to the data used in this project, such was used to help compare effectiveness amongst models to determine what strategy may be best for the real-time scraped data - this was done before the Twitter API was made available to our team.

The kaggle data file (See Twitter_NLP_Kaggle_Data.ipynb) analyzes a number of the popular natural language processing libraries and their effectiveness when 
dealing specifically with twitter data. The following three NLP libraries were analzyed, utilizing several different parameters in each to analyze the models' effectiveness. All three models were then compared to determine which would be best suited for this project:

- Blob Sentiment Model
   - rule-based model 
    - text represented as the sum of its words (i.e "bag-of-words" approach)
   - fairly simple NLP library taking in basics such as part of speech tagging, classification, etc 
   *(See https://textblob.readthedocs.io/en/dev/ for info)*
   
- Vader Sentiment Model (Valence Aware Dictionary for Sentiment Reasoning)
   - rule-based model 
   - empirically validated by multiple independent human judges 
   - uses word heuristics and recognizes word instensifiers, negations, etc, but cannot recognize typos (i.e overlooks misspelt words).
   *(See Vader github https://github.com/cjhutto/vaderSentiment)*
   
- Flair Sentiment Model
   - word embedding model 
    - words recognized in the form of a real-value vector where words close in promiximity in the vector space are assumed to have similar meaning.
   - accounts for spelling errors
   - pre-trained recurrent neural network accounting for word and letter sequencing 
   *(See Flair github https://github.com/flairNLP/flair)*

