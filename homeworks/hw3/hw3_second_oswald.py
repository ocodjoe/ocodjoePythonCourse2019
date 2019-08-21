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
WashU_followersstatuses =[]
for i in WashU_followers:
    WashU_followersstatuses.append(api.get_user(i).statuses_count)
    
WashU_followersstatuses 

max_value = max(WashU_followersstatuses)
max_index = WashU_followersstatuses.index(max_value)

api.get_user(WashU_followers[max_index]).name


#QUESTION 1B 
##Determining who among the 20 WashU followers has the highest number of followers
WashU_followers2 = []










