# RedditDatapipeline

# Overview

The purpose of this project is to get a general idea of the types of users who post on the Python subreddit. This pipeline draws data from reddit's api, and stores them inside a raw S3 bucket. This data is then transformed using pandas and restored in a second S3 bucket. CSV files are then copied over to postgres. Dashboard is created using plotly.



# Architecture

![Untitled presentation](https://user-images.githubusercontent.com/70300980/170851659-2b7ff1da-68b0-4089-ab16-f3bd672f803a.jpg)





# Relational tables









# Frameworks/Resources used
-AWS S3, for my Data lake, stored raw data 
-PostgreSQL as my data warehouse
-Apache Airflow as my Orchestration tool

Python Libraries
-PRAW to scrape data using api
-PANDAS to import csv files as dataframes and apply transformation
-Datetime for Airflow




