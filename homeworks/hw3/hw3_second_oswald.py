#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 20:33:37 2019

@author: oswaldcodjoe
"""

#QUESTION 1A

##Installing and loading the tweepy module
pip install tweepy
import tweepy

##Establishing the twitter API to be used by my program
twitter = imp.load_source('oswaldapp1','/Users/oswaldcodjoe/OneDrive - Washington University in St. Louis/Summer 19/Python/SecretAPIFolder/twitterAPI/start_twitter_oswald.py')
api = twitter.client

##Creating a user object called WashU
WashU = api.get_user('@WUSTL')

##Extracting a list of 20 followers of WashU
WashU_followers = []
for item in tweepy.Cursor(api.followers_ids,'@WUSTL').items(20): 
        WashU_followers.append(item) 

WashU_followers

##Determining who among the 20 WashU followers has the highest number of tweets
WashU_followersstatuses_count =[]
for i in WashU_followers:
    WashU_followersstatuses_count.append(api.get_user(i).statuses_count)
    
WashU_followersstatuses_count 

max_value = max(WashU_followersstatuses_count)
max_index = WashU_followersstatuses_count.index(max_value)

api.get_user(WashU_followers[max_index]).name


#QUESTION 1B 

##Determining who among the 20 WashU followers has the highest number of followers
WashU_followers_count = []
for i in WashU_followers:
    WashU_followers_count.append(api.get_user(i).followers_count)
    
WashU_followers_count  

max_value = max(WashU_followers_count)
max_index = WashU_followers_count.index(max_value)

api.get_user(WashU_followers[max_index]).name


#QUESTION 1C

##Determining who among the 20 that WashU follows has the highest number of followers.
WashU_friends = []
for item in tweepy.Cursor(api.friends_ids, '@WUSTL').items(20):
    WashU_friends.append(item) 

WashU_friends_followers_count = [] 
for i in WashU_friends:
    WashU_friends_followers_count.append(api.get_user(i).followers_count)

WashU_friends_followers_count

max_value = max(WashU_friends_followers_count)
max_index = WashU_friends_followers_count.index(max_value)

api.get_user(WashU_friends[max_index]).name

#QUESTION 1D

##Determining who among the 20 that WashU follows has the highest number of tweets by group.

WashU_friends_statuses_count = []
for i in WashU_friends:
    WashU_friends_statuses_count.append(api.get_user(i).statuses_count)

WashU_friends_statuses_count

max_value = max(WashU_friends_statuses_count)
max_index = WashU_friends_statuses_count.index(max_value)

api.get_user(WashU_friends[max_index]).name #this just gives friend with max tweets

#Grouping the 20 friends of WashU into layman, expert, and celebrity 

layman = []
expert = []
celebrity = []


for i in WashU_friends:
    if api.get_user(i).followers_count < 100:
        layman.append(api.get_user(i).id)
    
for i in WashU_friends:
    if 100 <= api.get_user(i).followers_count <= 1000:
        expert.append(api.get_user(i).id)
        
for i in WashU_friends:
    if api.get_user(i).followers_count > 1000:
        celebrity.append(api.get_user(i).id) 
        
       
#Determining which layman, expert, and celebrity have the most tweets.
        
layman_statuses_count = []        
for i in layman:
    layman_statuses_count.append(api.get_user(i).statuses_count)  

max_value1 = max(layman_statuses_count)
max_index1 = layman_statuses_count.index(max_value1)

"The layman with the most tweets is %s" %api.get_user(layman[max_index1]).name


expert_statuses_count = []
for i in expert:
    expert_statuses_count.append(api.get_user(i).statuses_count)
    
max_value2 = max(expert_statuses_count)
max_index2 = expert_statuses_count.index(max_value2)

"The expert with the most tweets is %s" %api.get_user(expert[max_index2]).name
   

celebrity_statuses_count = []
for i in celebrity:
    celebrity_statuses_count.append(api.get_user(i).statuses_count)

max_value3 = max(celebrity_statuses_count)
max_index3 = celebrity_statuses_count.index(max_value3)

"The celebrity with the most tweets is %s" %api.get_user(celebrity[max_index3]).name

    
#########################3   
        

##QUESTION 2A

# cont. here. 
