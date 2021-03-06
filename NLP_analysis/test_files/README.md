# Testing NLP 

The above files were used to test different NLP libraries on a mock kaggle dataset (see [Cleaned_Bitcoin_tweets.csv](https://github.com/findthefunction/goldendwarf/blob/main/NLP_analysis/test_files/Cleaned_Bitcoin_tweets.csv)). As there is a lull-period to gain API access to Twitter, this dataset was used to help develop a data pre-processing approach as well as NLP strategy for the project. 

The first file (See [NLP_practice.ipynb](https://github.com/findthefunction/goldendwarf/blob/main/NLP_analysis/test_files/NLP_practice.ipynb)) deals with data preprocessing and saves the cleaned data into a new dataframe with clean tweets. The second file (See [Twitter_NLP_Kaggle_Data.ipynb](https://github.com/findthefunction/goldendwarf/blob/main/NLP_analysis/test_files/Twitter_NLP_Kaggle_Data.ipynb)) analyzed a number of the popular natural language processing libraries and their effectiveness when 
dealing specifically with twitter data. The following three NLP libraries were analyzed, utilizing several different parameters in each to analyze the models' effectiveness. All three models were then compared to determine which would be best suited for the project:

## Blob Sentiment Model
- rule-based model 
   - text represented as the sum of its words (i.e "bag-of-words" approach)
- fairly simple NLP library taking in basics such as part of speech tagging, noun-phrase extraction, classification, etc.
   
 *(See https://textblob.readthedocs.io/en/dev/)*
   
## Vader Sentiment Model 
- (Valence Aware Dictionary for Sentiment Reasoning)
- rule-based model 
- empirically validated by multiple independent human judges 
- built in heuristics to recognize many syntactical elements such as word intensifiers, negations, conventional use of punctuation, a wide variety of slang typically used in social media contexts, utf-8 encoded emojis, etc
   - empirically validated gold-standard list of lexical features specifically attuned to micro-blog-like texts
      - lexical features are combined with five general rules thought to embody syntactical and grammitical conventions for the expression of sentiment and sentiment intensity within these contexts.
 
 *(See Vader github https://github.com/cjhutto/vaderSentiment)*
   
## Flair Sentiment Model
- word embedding model 
      - words recognized in the form of a real-value vector where words close in proximity in the vector space are assumed to have similar meaning.
- accounts for spelling errors
- pre-trained recurrent neural network accounting for word and letter sequencing 

*(See Flair github https://github.com/flairNLP/flair)*
