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

#Grouping the 20 that WashU follows into layman, expert, and celebrity
#But I got stuck so come back to this later

layman = []
expert = []
celebrity = []
    
for i in WashU_friends_followers_count:
    
    if i < 100:
        layman.append(i) 
    elif 100 <= i <= 1000:
        expert.append(i)
    elif i > 1000:
        celebrity.append(i)

max_value1 = max(layman)
max_index1 = layman.index(max_value1)

api.get_user(WashU_friends[max_index1]).name
api.get_user(WashU_friends[max_index1])    
    
layman
expert
celebrity
#########################3    
        

##QUESTION 2A

#
