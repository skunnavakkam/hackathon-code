
import sqlite3
import pandas as pd
import time
from sentiment import get_hashtags

path = "dataverse_files/112_Congress_Tweet_Archive.xlsx"

tweets_dict = {}
guide_df = pd.read_excel("dataverse_files/112_Tweets_Guide.xlsx")

for sheet in range(4):
    df = pd.read_excel(path, sheet)
    names = df.columns.values
    for name in names:
        
