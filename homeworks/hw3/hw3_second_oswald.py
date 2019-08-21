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

    
####################################################
        

##QUESTION 2A

# ##Creating a user object called PSC
PSC = api.get_user('@WUSTLPolisci')

##Extracting a list of IDs of 20 followers of PSC
PSC_followers = []
for item in tweepy.Cursor(api.followers_ids,'@WUSTLPolisci').items(20): 
        PSC_followers.append(item) 

##Extracting a list of IDS of 20 followers of each of the 20 followers of PSC        
PSC_followers2 = []
for i in PSC_followers:
    for j in tweepy.Cursor(api.followers_ids, i).items(20):
        PSC_followers2.append(j)
    
PSC_followers2 #Note: This list is not complete since some of the queries were 
               #unauthorized. Thus, twitter didn't allow me to fetch. 

#Grouping each of the followers of the followers into layman and expert
               
layman1 = []
expert1 = []


for i in PSC_followers2:
    if api.get_user(i).followers_count < 100:
        layman1.append(api.get_user(i).id)
    
for i in PSC_followers2:
    if 100 <= api.get_user(i).followers_count <= 1000:
        expert1.append(api.get_user(i).id)
        

#Determining which layman has the most tweets 
layman1_statuses_count = []        
for i in layman1:
    layman1_statuses_count.append(api.get_user(i).statuses_count)  

max_valueA = max(layman1_statuses_count)
max_indexA = layman1_statuses_count.index(max_valueA)

"The layman with the most tweets is %s" %api.get_user(layman1[max_indexA]).name

#Determining which expert has the most tweets
expert1_statuses_count = []
for i in expert1:
    expert1_statuses_count.append(api.get_user(i).statuses_count)
    
max_valueB = max(expert1_statuses_count)
max_indexB = expert1_statuses_count.index(max_valueB)

"The expert with the most tweets is %s" %api.get_user(expert1[max_indexB]).name
   


##QUESTION 2B

##Extracting a list of IDs of 20 friends of PSC
PSC_friends = []
for item in tweepy.Cursor(api.friends_ids,'@WUSTLPolisci').items(20): 
        PSC_friends.append(item) 


##Extracting a list of IDS of 20 friends of each of the 20 friends of PSC 
#Note: At this point it said I had reached the rate limit. 
PSC_friends2 = []
for i in PSC_friends:
    for j in tweepy.Cursor(api.friends_ids, i).items(20):
        PSC_friends2.append(j)

#Grouping each of the friends of the friends of PSC into layman and expert
#Note: It was taking longer than usual here so I stopped it. 
               
layman1 = []
expert1 = []


for i in PSC_friends2:
    if api.get_user(i).followers_count < 100:
        layman1.append(api.get_user(i).id)
    
for i in PSC_friends2:
    if 100 <= api.get_user(i).followers_count <= 1000:
        expert1.append(api.get_user(i).id)
        

#Determining which layman has the most tweets 
layman1_statuses_count = []        
for i in layman1:
    layman1_statuses_count.append(api.get_user(i).statuses_count)  

max_valueA = max(layman1_statuses_count)
max_indexA = layman1_statuses_count.index(max_valueA)

"The layman with the most tweets is %s" %api.get_user(layman1[max_indexA]).name


#Determining which expert has the most tweets
expert1_statuses_count = []
for i in expert1:
    expert1_statuses_count.append(api.get_user(i).statuses_count)
    
max_valueB = max(expert1_statuses_count)
max_indexB = expert1_statuses_count.index(max_valueB)

"The expert with the most tweets is %s" %api.get_user(expert1[max_indexB]).name

    
