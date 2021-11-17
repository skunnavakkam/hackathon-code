
import sqlite3
import pandas as pd
import time

Tweets = pd.read_excel("dataverse_files/112_Congress_Tweet_Archive.xlsx")

for name in Tweets:
    t = time.time()
    for tweet in Tweets[name]:
        if (type(tweet) != float and type(tweet) != int) and "lgbt" in tweet.lower():
            print(tweet)