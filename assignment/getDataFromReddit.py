import praw
import csv

# Step 1: Authenticate using API credentials
reddit = praw.Reddit(
    client_id="ndh6zXY0uY5cEKTh9VH3FA",  # Your Reddit client ID
    client_secret="gYgivvdVnjuA4FWW0cL1Ao1XerkG4Q",  # Your Reddit client secret
    user_agent="python:script:v1.0 (by u/Broad_Midnight_2077)",  # Example: 'python:script:v1.0 (by u/your_reddit_username)'
    username="fengying1028@gmail.com",  # Your Reddit username
    password="81531shjrxk"  # Your Reddit password
)
# import requests
# import requests.auth
# client_auth = requests.auth.HTTPBasicAuth('ndh6zXY0uY5cEKTh9VH3FA', 'gYgivvdVnjuA4FWW0cL1Ao1XerkG4Q')
# post_data = {"grant_type": "password", "username": "fengying1028@gmail.com", "password": "81531shjrxk"}
# headers = {"User-Agent": "python:script:v1.0 (by u/Broad_Midnight_2077)"}
# response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
# print(response.json())
try:
    user = reddit.user.me()  # 获取当前登录用户的信息
    print(f"Logged in as: {user.name}")
except Exception as e:
    print(f"An error occurred: {e}")

# # Step 2: Function to fetch Reddit posts and store in a CSV file
# def fetch_reddit_data(subreddit_name, search_word, num_posts=100):
#     # Create a CSV file to store the Reddit posts
#     csv_file = f"{search_word}_reddit_posts.csv"
#
#     # Open the file in write mode
#     with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerow(['Title', 'Author', 'Score', 'Subreddit', 'URL', 'Date', 'Comments'])  # Define column headers
#
#         # Search for posts using the API
#         subreddit = reddit.subreddit(subreddit_name)
#         for submission in subreddit.search(search_word, limit=num_posts):
#             title = submission.title
#             author = submission.author.name if submission.author else 'N/A'
#             score = submission.score
#             subreddit = submission.subreddit.display_name
#             url = submission.url
#             created_at = submission.created_utc
#             num_comments = submission.num_comments
#
#             # Write data to the CSV file
#             writer.writerow([title, author, score, subreddit, url, created_at, num_comments])
#
#     print(f"Downloaded {num_posts} posts related to '{search_word}' from r/{subreddit_name} into {csv_file}")
#
#
# # Step 3: Run the function to get the data
# subreddit_name = 'technology'  # Specify which subreddit to search in
# search_word = 'AI'  # Replace with your search word
# fetch_reddit_data(subreddit_name, search_word, num_posts=100)
