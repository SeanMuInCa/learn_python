import tweepy
import pandas as pd
import csv

client = tweepy.Client(bearer_token="AAAAAAAAAAAAAAAAAAAAAGLgwwEAAAAAtJke5Wg5Bo8IIffBJj9weMgKOIw%3DYo7FsBsCi4S45GiHte7jtmkvVfxhaShdImOfBlBpIDB3ZBOcti")


# Step 1: Search for tweets
query = "China"
response = client.search_recent_tweets(query=query, tweet_fields=["created_at", "text", "author_id"], max_results=100)

# Step 2: Extract data from the response
tweets = []
for tweet in response.data:
    tweets.append({
        "author_id": tweet.author_id,
        "created_at": tweet.created_at,
        "text": tweet.text
    })

# Step 3: Create a DataFrame
df = pd.DataFrame(tweets)

# Step 4: Save DataFrame to CSV
df.to_csv(f"{query}_tweets.csv", index=False)

print(f"Data saved to {query}_tweets.csv")