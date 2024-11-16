import os
from distutils.log import fatal
from operator import index
from re import search

import pandas as pd
from googleapiclient.discovery import build

API_KEY = 'AIzaSyCWJzSunMJBynlH7J1gPBYycRUqqiAGCQ0'

youtube = build('youtube', 'v3', developerKey=API_KEY)


search_keyword = 'program language'
search_response = youtube.search().list(q=search_keyword, part='id,snippet', maxResults=2).execute()


test = []
for i in search_response['items']:
    test.append(i['id']['videoId'])
test1 = []
for id in test:
    res = youtube.videos().list(part="snippet,contentDetails,statistics" ,id=id).execute()
    for item in res['items']:
        test1.append(item)
print(test1)
# search_results = search_response['items']
# while 'nextPageToken' in search_response:
#     next_page_token = search_response['nextPageToken']
#
#     # 使用nextPageToken获取下一页数据
#     search_response = youtube.search().list(
#         q=search_keyword,
#         part='id,snippet',
#         maxResults=50,
#         pageToken=next_page_token  # 使用nextPageToken请求下一批数据
#     ).execute()
#
#     # 将新获取的结果添加到列表
#     search_results += search_response['items']
# videos = []
# for search_result in search_results:
#     if search_result['id']['kind'] == 'youtube#video':
#         video = {
#             'id': search_result['id']['videoId'],
#             'title': search_result['snippet']['title'],
#             'description': search_result['snippet']['description'],
#             'publishedAt': search_result['snippet']['publishedAt'],
#             'channelId': search_result['snippet']['channelId'],
#             'channelTitle': search_result['snippet']['channelTitle'],
#         }
#         videos.append(video)
# df = pd.DataFrame(videos)
# df.to_csv('dataFromYoutube.csv', index=False)