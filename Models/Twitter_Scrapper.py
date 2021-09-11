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

