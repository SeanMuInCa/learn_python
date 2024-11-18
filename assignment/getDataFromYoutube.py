import pandas as pd
from googleapiclient.discovery import build

API_KEY = 'AIzaSyABXWVbt2Ybc7l89W9r77oFliPfIjz_bJU'

youtube = build('youtube', 'v3', developerKey=API_KEY)


search_keyword = 'china'
search_response = youtube.search().list(q=search_keyword, part='id,snippet', maxResults=2).execute()

search_results = search_response['items']
while 'nextPageToken' in search_response:
    next_page_token = search_response['nextPageToken']
    search_response = youtube.search().list(
        q=search_keyword,
        part='id,snippet',
        maxResults=50,
        pageToken=next_page_token
    ).execute()
    search_results += search_response['items']
videoIds = []
for i in search_results:
    if i['id']['kind'] == 'youtube#video':
        videoIds.append(i['id']['videoId'])

videos = []
for id in videoIds:
    res = youtube.videos().list(part="snippet,contentDetails,statistics" ,id=id).execute()
    for item in res['items']:
        if item['kind'] == 'youtube#video':
            video = {
            'id': item.get('id', None),
            'title': item['snippet'].get('title', None),
            'description': item['snippet'].get('description', None),
            'publishedAt': item['snippet'].get('publishedAt', None),
            'channelId': item['snippet'].get('channelId', None),
            'channelTitle': item['snippet'].get('channelTitle', None),
            'tags': item['snippet'].get('tags', []),
            'categoryId': item['snippet'].get('categoryId', None),
            'defaultLanguage': item['snippet'].get('defaultLanguage', None),
            'duration': item['contentDetails'].get('duration', None),
            'viewCount': item['statistics'].get('viewCount', None),
            'likeCount': item['statistics'].get('likeCount', None),
            'favoriteCount': item['statistics'].get('favoriteCount', None),
            'commentCount': item['statistics'].get('commentCount', None)
            }
            videos.append(video)
df = pd.DataFrame(videos)
df.to_csv(f'dataFromYoutube_{search_keyword}.csv', index=False)
