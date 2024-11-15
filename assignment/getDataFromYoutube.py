import os
from re import search

import pandas as pd
from googleapiclient.discovery import build

API_KEY = 'AIzaSyCWJzSunMJBynlH7J1gPBYycRUqqiAGCQ0'

youtube = build('youtube', 'v3', developerKey=API_KEY)

search_keyword = 'china'
search_response = youtube.search().list(q=search_keyword, part='id,snippet', maxResults=10).execute()
search_result = search_response['items']
