
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

s3 = boto3.client('s3')


#first task. Grabs data from api, stores them into a csv, and pushes to S3
def datatocsv():
    posts_dict = {"Title": [], "Post Text": [],
              "ID": [], "Score": [],
              "Total Comments": [], "Post URL": []
              }
    for post in posts:
        # Title of each post
        posts_dict["Title"].append(post.title)
     
        # Text inside a post
        posts_dict["Post Text"].append(post.selftext)
     
        # Unique ID of each post
        posts_dict["ID"].append(post.id)
     
        # The score of a post
        posts_dict["Score"].append(post.score)
     
        # Total number of comments inside the post
        posts_dict["Total Comments"].append(post.num_comments)
     
        # URL of each post
        posts_dict["Post URL"].append(post.url)


    #Turns a python dictionary into a Pandas Dataframe
    toppoststoday  = pd.DataFrame(posts_dict)
    toppoststoday.to_csv("Top Posts.csv", index=True)
    #Grabs current datatime
    now = datetime.datetime.now()
    name = 'Top Posts.csv '
    s3.upload_file('/Users/caryk/Desktop/Pipeline/Top Posts.csv','imdoingthistolearn',name)







#second task, pulling from S3 and transforming csv files using pandas


def transformdata():
    #check if file is present in S3
    














































posts_dict = {"Title": [], "Post Text": [],
              "ID": [], "Score": [],
              "Total Comments": [], "Post URL": []
              }



