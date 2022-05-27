import requests
import os
import json
import tweepy

import numpy as np # linear algebra

# Libraries and packages for NLP
import nltk


file = open('.gitignore')
lines = file.readlines()
print(lines)
elems = []
for i in lines:
    index = i.find("\n")
    i = i[0:index]
    elems.append(i)


#auth = tweepy.OAuth2UserHandler(
#   elems[0], elems[1], elems[2], elems[3]
#)
client = tweepy.Client(elems[0])

print(client)

def extract_tweets(tweets):
    tweet_list = []
    #print(tweets,"\n")
    for i in tweets:
        tweet_list.append(i.text)
    return tweet_list

def aggregate_tweets(user_name, days=0):
    tweet_list = []
    first = True
    user_id = client.get_user(username = user_name).data.id
    count = 0
    print(user_id)
    next_token = ""
    found_token = False
    tot = 0
    while count<10:
       
        try:
            if (found_token == False):
                response = (client.get_users_mentions(id = user_id,max_results=5))
               
                next_token = response.meta['next_token']
                found_token = True
                tot += 1
                continue
            else:
   
                response_tweets = client.get_users_mentions(id = user_id,max_results=5,pagination_token = next_token)
                if (response_tweets.data == None):
                    tot+= 1
                    continue
                
                next_token = response_tweets.meta['next_token']
                tweet_list += extract_tweets(client.get_users_mentions(id = user_id,max_results=5,pagination_token = next_token)[0])
            count += 1
            
        except:
            traceback.print_exc()
            break
    print(tot)
    return tweet_list
                
        


