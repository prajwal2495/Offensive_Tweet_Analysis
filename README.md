# Offensive Language indentification in tweets
## An automated model trained to detect whether a tweet is offensive or not on multiple levels of classification. ( in development )

Digital bullying is happening on a daily basis and all of us are facing in form or another on social media. 

Proposing a solution to tackle this problem by generating an automated tool that uses ML algorithmns and techniques to detect these offensive languages in our cases specifically in tweets and then decide whether the tweet was targeted, and if so, classifying the target into more labels.

## Twitter Scrapper

This is a simple twitter scrapper which uses tweepy library of python to extract tweets based on the query, which is a list of Marathi phrases.
We use our own API_KEY, API_SECRET_KEY, ACCESS_TOKEN and ACCESS_SECRET_KEY to auntheticate the API and make a call to it.
All the searched ad extracted tweets are stored in a JSON file, the format is as follows.
```
 with open(filename, 'a') as f:
        f.write('{"data": [')
        for tweet in tweets:
            json.dump(tweet._json, f)
            f.write(',\n')
        f.write(']}')
```


## Text Cleaning
We have developed a simple text cleaning python script which is used to Lowercase all the texts, remove urls, remove mentions and replace them with a place holder @USER, since our aim in this project is to find offensive tweets of Marathi any English words in between is being removed, and all the special characters are being removed.
A dictionary called clean_config has been created 
```
clean_config = {
    'remove_url': True,
    'remove_mentions': True,
    'decode_utf8': True,
    'lowercase': True,
    'remove_english':True,
    'remove_specials':True,
    'add_USER_tag':True
    }
```
The main aim behind this dictionary is to give more freedom in cleaning, toggling between True and False will make sure that those cleanign aspects are executed or not.
The emojis in the text are being removed as they dont provide any meaningful insights for our models in future implementation to learn about offensive language.
