# -*- coding: utf-8 -*-
"""
Created on Fri Apr 03 16:35:42 2020

@author: deadp
"""
""" Written in Python3"""

import praw
import time
from praw.models import MoreComments
import csv
from datetime import datetime
import time
import os 
import pandas as pd

start = time.time()


# two_months_timestamp = start - (60*60*24*20)
try:

    os.mkdir('reddit')
    
except:
    print ("Directory exists")


#Enter your credentials here!

reddit = praw.Reddit(client_id='#######',
                     client_secret='######',
                     user_agent='###',
                     username='#####',
                     password='######')

i=0

#Add a subreddit of your choice here 
subreddit = reddit.subreddit('coronavirus')   

print ("Iterating through coronavirus subreddit")

for submission in subreddit.hot(limit=int(time.time())):
    sub_entries={}
    subData=[]
    Comment_ID=[]
    Comment_ParentID=[]
    Comment_body =[]
    headers= []
    TIME =[]
    title = (submission.title)  # Output: the submission's title
    score = (submission.score)  # Output: the submission's score
    unique=(submission.id)     # Output: the submission's ID
    link = ("https://www.reddit.com"+submission.permalink)
    
    # print (link)
    author = submission.author 
    upratio = submission.upvote_ratio
    topcommsCnt = len(submission.comments)
    allcommsCnt = len(submission.comments.list())
    # created = datetime.datetime.fromtimestamp(submission.created) 
    flair = submission.flair
    # subData.append((unique,title,link,author,score,created,upratio,topcommsCnt,allcommsCnt,flair))
    sub_entries[unique]=subData
    # print (link)
    
    submission = reddit.submission(url=link)
    submission.comment_sort = 'new'
    
    # print (submission)
    
    submission.comments.replace_more(limit=0)
    
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    # path=os.cwdr()
    my_file=os.path.join(THIS_FOLDER,'reddit', unique +'.csv')
    
    if os.path.exists(my_file):
        print ("Already exists")
    else:
        
        for comment in submission.comments.list():
            # print (comment.body)
                # print (commentb)      
            Comment_body.append((comment.body).replace('\n',''))
                # print (commentb)
                # print ("-"*20)
                # print (comment.id)
            Comment_ID.append(comment.id)
                # print (comment.parent())
            comtime = comment.created_utc
            stamp=datetime.fromtimestamp(comtime)
                # print (stamp)
            TIME.append(stamp)
            Comment_ParentID.append(comment.parent())
                # print ("-"*20)
        
      
        df = pd.DataFrame()
        df['Comments'] = Comment_body
        df['Comment_Id']= Comment_ID
        df['Comment_ParentId']=Comment_ParentID
        df['Timestamp']= TIME
        
        print ("Writing the output")
        
        with open(my_file,'a',encoding="utf-8") as f:
    # f.write(',,,\n')
            f.write('Title: {}, URL: {} ups: {}, downs: {}, subid: {}'.format(submission.title,("https://www.reddit.com"+submission.permalink),submission.ups,submission.downs,submission.id))
    
            df.to_csv(my_file,index=False)
            
            i+=1
            print ("Delaying 10 seconds")
            time.sleep(10)
            
        print ("Total number of files written: " +str(i))
    
        
        
        
        