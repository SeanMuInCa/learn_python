import os
from distutils.log import fatal
from operator import index
from re import search

import pandas as pd
from googleapiclient.discovery import build

API_KEY = 'AIzaSyCWJzSunMJBynlH7J1gPBYycRUqqiAGCQ0'

youtube = build('youtube', 'v3', developerKey=API_KEY)

search_keyword = 'china'
search_response = youtube.search().list(q=search_keyword, part='id,snippet', maxResults=10).execute()
search_results = search_response['items']

videos = []
for search_result in search_results:
    if search_result['id']['kind'] == 'youtube#video':
        video = {
            'id': search_result['id']['videoId'],
            'title': search_result['snippet']['title'],
            'description': search_result['snippet']['description'],
            'publishedAt': search_result['snippet']['publishedAt'],
            'channelId': search_result['snippet']['channelId'],
            'channelTitle': search_result['snippet']['channelTitle'],
        }
        videos.append(video)
df = pd.DataFrame(videos)
df.to_csv('dataFromYoutube.csv', index=False)