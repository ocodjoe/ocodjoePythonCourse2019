#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 14:14:29 2019

@author: oswaldcodjoe
"""
###FIRST ATTEMPT

##Importing all relevant modules
from bs4 import BeautifulSoup
import urllib.request
import re
import csv
import unicodedata 


#Creating dictionary to store info. about petitions
with open("petitions_data.csv","w") as f:
    dataset = csv.DictWriter(f, fieldnames = ("Title","Published Date","Issues","# of Signatures"))
    dataset.writeheader()
    
    web_address = "https://petitions.whitehouse.gov/?page=1"
    web_page = urllib.request.urlopen(web_address)                                      
    html = BeautifulSoup(web_page.read())
    all_petitions = html.find_all("div", {"class" :"views-row"})

    for i in all_petitions:
        extract = {}
        extract["Title"] = i.article.h3.get_text() 
        extract["# of Signatures"] = i.article.find('span',{'class':'signatures-number'}).get_text()
        dataset.writerow(extract) 
    

#Note: So far, I've been able to get title, and number of signatures but to get
#published date, I need to go to each petition's webpage. I can repeat the code above
#for all 4 pages -- I just have to change web_address. Forget about issues for now
#I think it's the same as titles.... so put 'same as title' or do something. 


#i.article.h3.get_text()
#all_petitions[0].article.get_text() 
#all_petitions[0].article.h3.get_text()
#all_petitions[0].article.h6.get_text() 


#all_petitions[0]
#i.article.find('div', {'class':'signatures-text-container'}).get_text()
#all_petitions[0].article.find('div',{'class':'signatures-text-container'}).get_text()
#all_petitions[0].article.find('span',{'class':'signatures-number'}).get_text()
        
#######################Okay now I'm writing code (building on above) that clicks each petition####
#Oh I have an idea: write code inside the for loop that opens each petition

##### SECOND ATTEMPT
        
from bs4 import BeautifulSoup
import urllib.request
import re
import csv
import unicodedata


#Creating dictionary to store info. about petitions
with open("petitions_data.csv","w") as f:
    dataset = csv.DictWriter(f, fieldnames = ("Title","Published Date","Issues","# of Signatures"))
    dataset.writeheader()
    
    web_address = "https://petitions.whitehouse.gov/?page=1"
    web_page = urllib.request.urlopen(web_address)                                      
    html = BeautifulSoup(web_page.read())
    all_petitions = html.find_all("div", {"class" :"views-row"})

    for i in all_petitions:
        extract = {}
        extract["Title"] = i.article.h3.get_text() 
        extract["# of Signatures"] = i.article.find('span',{'class':'signatures-number'}).get_text()
        dataset.writerow(extract) 
        
        
        
#This part is for clicking each petition and extracting content. But I'm developing
#the code outside the loop for now.
        
###############ATTEMPT 3 #########################
#New idea: Follow the following steps:
        
# Click on one petition and use it's url to extract relevant info like you did in 
  #attempt 1
# Figure out a way to get the urls of all the petitions from the home page, and store
  #them in a list.
# Figure out a way to apply step 1 to each of the urls in the list.
# Final step, figure out a way to figure out a way to apply step 1 to each of the
  #urls in each of the 4 pages containing 20 or so petitions.  
  





