
import sqlite3
import pandas as pd
import time
from sentiment import get_hashtags

path = "dataverse_files/113_Congress_Tweet_Archive.xlsx"

def analyse_tags(Tweets) -> dict:
    tdict = {}
    for name in Tweets:
        t = time.time()
        for tweet in Tweets[name]:
            if (type(tweet) != float and type(tweet) != int):
                
                tags = get_hashtags(tweet)
                
                for tag in tags:
                    if tag in tdict:
                        tdict[tag.lower()] += 1
                    else:
                        tdict[tag.lower()] = 1
    return tdict
                        
tags_dict = {}

for i in range(4):
    d = analyse_tags(pd.read_excel(path, i))
    for key, value in d.items():
        if key in tags_dict:
            tags_dict[key] += value
        else:
            tags_dict[key] = value
                                            
with open('tags_dict113.txt', 'a') as f:
    for key in sorted(tags_dict, key=tags_dict.get, reverse = True):
        f.write(f'{key}: {tags_dict[key]} \n')