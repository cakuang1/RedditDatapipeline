import pandas as pd

import datetime
import praw
import boto3






# creates praw instance
reddit_read_only = praw.Reddit(client_id="Ka-lqmQSQHtRKZiy60-yaA",         # your client id
                               client_secret="Eff1G7qnTA4wIMxDczrmqmyasg_BKg",      # your client secret
                               user_agent="Askredscraper") 




# Grabbing the subreddit object
subreddit = reddit_read_only.subreddit("Python")
 
# Grabbing the top posts of the day

posts = subreddit.top("day")


for post in posts:
    redditorinstance = post.author



    print(redditorinstance.comments.new())



