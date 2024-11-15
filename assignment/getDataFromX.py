import tweepy
import pandas as pd

client = tweepy.Client(bearer_token="AAAAAAAAAAAAAAAAAAAAAGLgwwEAAAAAtJke5Wg5Bo8IIffBJj9weMgKOIw%3DYo7FsBsCi4S45GiHte7jtmkvVfxhaShdImOfBlBpIDB3ZBOcti")



query = "China"
response = client.search_recent_tweets(query=query, tweet_fields=["created_at", "text", "author_id",'id'], max_results=100)


tweets = []
for tweet in response.data:
    tweets.append({
        "author_id": tweet.author_id,
        "created_at": tweet.created_at,
        "text": tweet.text,

    })


df = pd.DataFrame(tweets)


df.to_csv(f"{query}_tweets.csv", index=False)

print(f"Data saved to {query}_tweets.csv")