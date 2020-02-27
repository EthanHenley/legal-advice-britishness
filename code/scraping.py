# -*- coding: utf-8 -*-
"""
Scraping Script for project_3

Created on Mon Jan 27 12:35:35 2020
"""

import pandas as pd
import datetime as dt
import time
import requests

# format requests
subs = 'legaladvice', 'legaladviceuk'

# a function defined by instructors for convenient pushshift querying
# demonstrated by Thomas Ludlow
def query_pushshift(subreddit, kind='submission', skip=30, times=7, 
                    subfield = ['title', 'selftext', 'subreddit', 
                                'created_utc', 'author', 'num_comments', 
                                'score', 'is_self'],
                    comfields = ['body', 'score', 'created_utc']):
    # slightly changed stem formatting
    stem = f"https://api.pushshift.io/reddit/search/{kind}" + \
    f"/?subreddit={subreddit}&size=500"
    mylist = []
    for x in range(times): # altered to go up to present day
        URL = "{}&after={}d".format(stem, skip * x)
        print(URL)
        response = requests.get(URL)
        print(response.status_code)
        assert response.status_code == 200
        mine = response.json()['data']
        df = pd.DataFrame.from_dict(mine)
        mylist.append(df)
        time.sleep(2)
    full = pd.concat(mylist, sort=False)
    if kind == "submission":
        full = full[subfield]
        full = full.drop_duplicates()
        full = full.loc[full['is_self'] == True]
    def get_date(created):
        return dt.date.fromtimestamp(created)
    _timestamp = full["created_utc"].apply(get_date)
    full['timestamp'] = _timestamp
    print(full.shape)
    return full 

# run the queries and concatenate them
df = pd.concat([query_pushshift(sub) for sub in subs])

# output
df.to_csv('../data/scraped.csv',index=False)