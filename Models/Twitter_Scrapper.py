import tweepy
from tweepy import OAuthHandler
import json
import datetime as dt
import time
import os
import sys


'''
In order to use this script you should register a data-mining application
with Twitter.  Good instructions for doing so can be found here:
http://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/

After doing this you can copy and paste your unique consumer key,
consumer secret, access token, and access secret into the load_api()
function below.

The main() function can be run by executing the command: 
python twitter_search.py

We used Python 3 and tweepy version 3.5.0.  You will also need the other
packages imported above.
'''

'''
Bearer Token
AAAAAAAAAAAAAAAAAAAAAAtpRgEAAAAALTJaSmQeisuVnghCHe9VVJGQyH4%3Dh1KDuVPhJySsZ8zS0fBwwWyRJJKVVHNuuAds1WTjT0e1SqTS7L

API/consumer key 
S7DciRFX45Oj6r88OhrAtLVcO

API/consumer secret key
7se4lB1eLBfdpZ95gKhvwGF7YuUhmJHlA0YwytHaheRHvDBXhF

Access token
306175074-GFIFZBvOZ72Edj7fgDhw0XyXcoztXKmYQhVL75Jk

Access token secret
85ieYgEPU8qbkKJXhoryV1hI4rjsXhUpSmf6E6NPayIEU

'''


def load_api():
    ''' Function that loads the twitter API after authorizing the user. '''

    consumer_key = 'aAXk7BfNJMIu7MWnGyqY5mnQ6'
    consumer_secret = 'kKa6EIfb7T1NxHurIWQ2r7cH3fKOR8X7St2tECUZmkCOI4AEVG'
    access_token = '3221158459-H7gxfAjwKpTfmCJkcurm8gd7bJOzySo6WixLVa1'
    access_secret = 'fawDcbdZiGfGyU0TcQ6aIXbO8pkXSRgsjMOiGjLQs0paQ'
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    # load the twitter API via tweepy
    return tweepy.API(auth)

def tweet_search(api, query, max_tweets, max_id, since_id, geocode):
    ''' Function that takes in a search string 'query', the maximum
        number of tweets 'max_tweets', and the minimum (i.e., starting)
        tweet id. It returns a list of tweepy.models.Status objects. '''

    searched_tweets = []
    while len(searched_tweets) < max_tweets:
        remaining_tweets = max_tweets - len(searched_tweets)
        try:
            new_tweets = api.search(q=query, count=remaining_tweets,
                                    since_id=str(since_id),
                                    max_id=str(max_id - 1))
            #                                    geocode=geocode)
            print('found', len(new_tweets), 'tweets')
            if not new_tweets:
                print('no tweets found')
                break
            searched_tweets.extend(new_tweets)
            max_id = new_tweets[-1].id
        except tweepy.TweepError:
            print('exception raised, waiting 15 minutes')
            print('(until:', dt.datetime.now() + dt.timedelta(minutes=15), ')')
            time.sleep(15 * 60)
            break  # stop the loop
    return searched_tweets, max_id


def get_tweet_id(api, date='', days_ago=9, query='a'):
    ''' Function that gets the ID of a tweet. This ID can then be
        used as a 'starting point' from which to search. The query is
        required and has been set to a commonly used word by default.
        The variable 'days_ago' has been initialized to the maximum
        amount we are able to search back in time (9).'''

    if date:
        # return an ID from the start of the given day
        td = date + dt.timedelta(days=1)
        tweet_date = '{0}-{1:0>2}-{2:0>2}'.format(td.year, td.month, td.day)
        tweet = api.search(q=query, count=1, until=tweet_date, lang='mr')
    else:
        # return an ID from __ days ago
        td = dt.datetime.now() - dt.timedelta(days=days_ago)
        tweet_date = '{0}-{1:0>2}-{2:0>2}'.format(td.year, td.month, td.day)
        # get list of up to 10 tweets
        tweet = api.search(q=query, count=5, until=tweet_date, lang='mr')
        print('search limit (start/stop):', tweet[0].created_at)
        # return the id of the first tweet in the list
        return tweet[0].id


def write_tweets(tweets, filename):
    ''' Function that appends tweets to a file. '''

    with open(filename, 'a') as f:
        f.write('{"data": [')
        for tweet in tweets:
            json.dump(tweet._json, f)
            f.write(',\n')
        f.write(']}')
