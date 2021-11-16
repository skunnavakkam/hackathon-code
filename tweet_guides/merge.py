
# code to merge the three csv's of information into a single csv/dict

import pandas as pd

HouseTweetGuide113 = pd.read_csv('113_House_Tweet_Guide.csv')
SenateTweetGuide113 = pd.read_csv('113_Senate_Tweet_Guide.csv')
TweetGuide112 = pd.read_csv('112_Tweet_Guide.csv')

for index, handle in enumerate(TweetGuide112["Twitter Handle"]):
    if type(handle) == float or "(" in handle or handle == "NTA":
        continue 
    
    handle = handle.strip()