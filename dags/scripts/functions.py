
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
    posts_dict = {"Subreddit":[], "Title": [], "Post Text": [],
              "ID": [], "Score": [],
              "Total Comments": [], "Post URL": []
              }
    for post in posts:
        # Author of each post

        posts_dict["AuthorID"].append(post.author.name)

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

    # Grab redditor data
def booleaninfo():
    boo_dict = {"AuthorID":[], "employee": [], "verified": [],
            "mod": [], "gold": []
            }
    for post in posts:
        boo_dict["AuthorID"].append(post.author.name)

        boo_dict["employee"].append(post.author.is_employee)
        # Text inside a post
        boo_dict["verified"].append(post.author.has_verified_email)
     
        # Unique ID of each post
        boo_dict["mod"].append(post.author.is_mod)
     
        # The score of a post
        boo_dict["gold"].append(post.author.is_gold)
    
    boo  = pd.DataFrame(boo_dict)
    boo.to_csv("boolean.csv", index=True)
    s3.upload_file('/Users/caryk/Desktop/Pipeline/boolean.csv','imdoingthistolearn','boolean.csv')





def numericalinfo():
    num_dict= {"AuthorID":[], "commentkarma": [], "linkkarma": [],
              }
    for post in posts:
        num_dict["AuthorID"].append(post.author.name)
        num_dict["commentkarma"].append(post.author.comment_karma)
        num_dict["linkkarma"].append(post.author.link_karma)


    
    num  = pd.DataFrame(num_dict)
    num.to_csv("num.csv", index=True)
    s3.upload_file('/Users/caryk/Desktop/Pipeline/num.csv','imdoingthistolearn','num.csv')


        

















































posts_dict = {"Title": [], "Post Text": [],
              "ID": [], "Score": [],
              "Total Comments": [], "Post URL": []
              }



