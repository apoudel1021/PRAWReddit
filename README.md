# Quick Introduction on PRAW: 

PRAW: The Python Reddit API Wrapper

PRAW supports above Python 3.5. 

For installing PRAW do:
```python
pip install praw 
```
(might have to use pip3)


You should have a reddit account in order to access Reddit API

##### Visit here to get your own credentials: 

[https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps]


##### For more info on PRAW and its uses, here's the documentation for the API. 

[https://praw.readthedocs.io/en/latest/getting_started/quick_start.html]


# Goal of the project:

To get all the submission from a specific subreddit with all the comments and their meta-data in a pandas dataframe. 

You can have a look at the data inside the reddit folder, which contains some of the sample posts and their comments collected through the subreddit /r/coronavirus. 

### Limitation with PRAW:
	1.It does not allow the use of timestamp, so you won't be able to get the submission of your desired date or time period. 
	2.It does not allow you to get more than 500-1000 submissions at a time. 
	3.From my experience, it provides you with approx. 250 submissions with subreddit.hot(), and more approx 1000 with 
	subreddit.top()


### Overcoming the limitation:

We will be making use of PushShift API and using PRAW together. Will be updating soon. 



