# Sentiment analysis: Narendra Modi

This repository contains code for doing sentiment analysis on the data of twitter based on recent tweets on NARENDRA MODI, the Prime Minister of India.
Following are the files and scripts :

##negative.txt & positive.txt
- contains negative and positive reviews to be used later for sentiment analysis.

##sentiment.py
- Training selected classifiers using negative.txt and positive.txt
- Dumping them in pickle files to be used later.

##sentimentanalysis.py
- Creating module to be used for sentiment analysis.
- The best classifier will be used out of all.

##twitter.py
- This contains the code for using tweets on 'Narendra Modi' .
- Each tweet is given a sentiment 'pos' or 'neg' using module sentimentanalysis.py
- The sentiment value is saved in a text file.

##testplotting.py
- Live graph streaming using module matplotlib to show trend in sentiments.

###NOTE:
- The module 'mytwitterkeys' is created so that my personal twitter keys remain private.
- Also I have not included twitter.txt here for privacy.
