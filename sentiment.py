
import re
from collections import namedtuple
from textblob import TextBlob
from datetime import datetime

Tweet = namedtuple('Tweet', ['Text', 'Categories', 'Subjectivity', 'Polarity', 'Year'])

categories = ['Cyber', 'Women\'s Rights', 'LGBT issues', 'Foreign Relations', 'Gun Control', 'Education', 'Constitution', 'Healthcare']

# key = {Cyber: 0
#        Women's Rights: 1,
#        LGBT issues: 2,
#        Foreign Relations: 3,
#        Gun Control: 4,
#        Education: 5,
#        Constitution: 6,
#        Health: 7}

tag_dict = {'2nd': 4,
        'internet': 0,
        'china': 3,
        'speech': 6,
        'shooting': 4,
        'troops': 3,
        'war': 3,
        'gay': 2,
        'terror': 3,
        'health': 7,
        'obamacare': 7,
        'schools': 5,
        'teachers': 5,
        'equal pay': 1,
        'lgbt': 2,
        'women': 15,
        'victim': 1,
        'gun': 4,
        'transgender': 2,
        'edu': 5
        }

get_hashtags = lambda x: re.findall('#[A-z0-9]+', x)

def analyse_tweet(tweet: str) -> Tweet:
    
    TweetBlob = TextBlob(tweet)
    
    sentiment = TweetBlob.sentiment
    subjectivity, polarity = sentiment.subjectivity, sentiment.polarity
    
    datestring = tweet[-13:-1]
    print(datestring)
    date = datetime.strptime(datestring, "%b %d, %Y")
    
    tags = set()
    for key, value in tag_dict.items():
        if key in tweet: tags.add(value)
    
    return Tweet(tweet, tags, subjectivity, polarity, date.year)
    
def store_analysis(tweet: Tweet):
    
    pass

def load_politician(tweets: list):
    for tweet in tweets:
        data = analyse_tweet(tweet)
        

        