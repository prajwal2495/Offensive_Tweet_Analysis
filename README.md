# Offensive Language indentification in tweets
## An automated model trained to detect whether a tweet is offensive or not on multiple levels of classification.

Digital bullying is happening on a daily basis and all of us are facing in form or another on social media. 

Proposing a solution to tackle this problem by generating an automated tool that uses ML algorithmns and techniques to detect these offensive languages in our cases specifically in tweets and then decide whether the tweet was targeted, and if so, classifying the target into more labels.

## Twitter Scrapper

This is a simple twitter scrapper which uses tweepy library of python to extract tweets based on the query, which is a list of Marathi phrases.
We use our own consumer_key, consumer_secret, access_token and access_secret to auntheticate the API and make a call to it.
All the searched ad extracted tweets are stored in a JSON file, the format is as follows.
```
 with open(filename, 'a') as f:
        f.write('{"data": [')
        for tweet in tweets:
            json.dump(tweet._json, f)
            f.write(',\n')
        f.write(']}')
```
