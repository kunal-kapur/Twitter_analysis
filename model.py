#Python file to make it easier to transfer

from find_user import aggregate_tweets
from cleaning import tokenize

from sklearn.naive_bayes import BernoulliNB
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

user_mention_tweets = aggregate_tweets("elonmusk")
tokenized_tweets = []
for i in user_mention_tweets:
    tokenized_tweets.append(tokenize(i))
#print(tokenized_tweets)

#Verifying it can be read
model = None
with open('model.pkl', 'rb') as inp:
    model = pickle.load(inp)

vector = TfidfVectorizer(tokenized_tweets)
# print(type(model))
# model.predict(tokenized_tweets)



