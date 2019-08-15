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
        
#####Changing work directory before I proceed 
import os
os.getcwd()
os.chdir('/Users/oswaldcodjoe/OneDrive - Washington University in St. Louis/Summer 19/Python/ocodjoePythonCourse2019/homeworks/hw2')

###############ATTEMPT 3 #########################
#New idea: Follow the following steps:
        
# 1: Click on one petition and use it's url to extract relevant info like you did in 
  #attempt 1
# 2: Figure out a way to get the urls of all the petitions from the home page, and store
  #them in a list.
# 3: Figure out a way to apply step 1 to each of the urls in the list.
# 4: Final step, figure out a way to figure out a way to apply step 1 to each of the
  #urls in each of the 4 pages containing 20 or so petitions.  
  
#Step1: Done.

from bs4 import BeautifulSoup
import urllib.request
import re
import csv
import unicodedata


with open("petitions_data.csv","w") as f:
    dataset = csv.DictWriter(f, fieldnames = ("Title","Published Date","Issues","# of Signatures"))
    dataset.writeheader() 
    
    web_address = "https://petitions.whitehouse.gov/petition/condemn-indias-denial-justice-victims-november-1984-sikh-genocide"
    web_page = urllib.request.urlopen(web_address)                                      
    html = BeautifulSoup(web_page.read())
    extract = {}
    extract["Title"] = html.find('h1',{'class':'title'}).get_text()
    date1 = html.find('h4',{'class':'petition-attribution'}).get_text()
    date2 = date1.split()
    extract["Published Date"] = ' '.join(date2[4:])
    extract["Issues"] = "Same as title"
    signatures = html.find('div',{'class':'signatures-text-container'}).get_text()
    signatures1 = signatures.split()
    extract["# of Signatures"] = signatures1[0]
    
    dataset.writerow(extract)
    

#Step 2: Extract url of each petition, put into a list, then perform step 1 for each url.
  #note: you just have to add a row to the already written csv. Think and proceed. 
  #Try step 1 with a few different links first -- to see if all the petitions have the same
  #page organization. 
    
  with open("petitions_data.csv","w") as f:
    dataset = csv.DictWriter(f, fieldnames = ("Title","Published Date","Issues","# of Signatures"))
    dataset.writeheader() 
    
    links = ["https://petitions.whitehouse.gov/petition/condemn-indias-denial-justice-victims-november-1984-sikh-genocide", 
          "https://petitions.whitehouse.gov/petition/stop-collective-punishment-minorities-south-africa"]   
    
    for i in range(0,2):
        web_address = links[i]
   
        web_page = urllib.request.urlopen(web_address)                                      
        html = BeautifulSoup(web_page.read())
        ex = {}
        ex["Title"] = html.find('h1',{'class':'title'}).get_text()
        date1 = html.find('h4',{'class':'petition-attribution'}).get_text()
        date2 = date1.split()
        ex["Published Date"] = ' '.join(date2[4:])
        ex["Issues"] = "Same as title"
        signatures = html.find('div',{'class':'signatures-text-container'}).get_text()
        signatures1 = signatures.split()
        ex["# of Signatures"] = signatures1[0]
    
        dataset.writerow(ex)
  
 
####Still on step 2. Okay so now that I know putting the urls of each petition in a list works,
##I'm going to go ahead and extract the urls into a list. 
address = "https://petitions.whitehouse.gov/#signapetition"
page = urllib.request.urlopen(address)
html_1 = BeautifulSoup(page.read())
links_a = html_1.find_all('a')
links_b = links_a[12:51]

for i in range(0,26):
    link = 'https://petitions.whitehouse.gov/%s' %links_b[i]['href']
    #print(link)
    #urllib.request.urlopen('https://petitions.whitehouse.gov/%s' %links_b[i]['href'])

#######Okay step 3:  so now I'm incorporating the above into step 2. 

with open("petitions_data.csv","w") as f:
    dataset = csv.DictWriter(f, fieldnames = ("Title","Published Date","Issues","# of Signatures"))
    dataset.writeheader() 
    
    address = "https://petitions.whitehouse.gov/#signapetition"
    page = urllib.request.urlopen(address)
    html_1 = BeautifulSoup(page.read())
    links_a = html_1.find_all('a')
    links_b = links_a[12:51]
    
    for i in range(0,39):
        #urllib.request.urlopen('https://petitions.whitehouse.gov/%s' %links_b[i]['href'])
        web_address = 'https://petitions.whitehouse.gov/%s' %links_b[i]['href']
   
        web_page = urllib.request.urlopen(web_address)                                      
        html = BeautifulSoup(web_page.read())
        ex = {}
        ex["Title"] = html.find('h1',{'class':'title'}).get_text()
        date1 = html.find('h4',{'class':'petition-attribution'}).get_text()
        date2 = date1.split()
        ex["Published Date"] = ' '.join(date2[4:])
        ex["Issues"] = "Same as title"
        signatures = html.find('div',{'class':'signatures-text-container'}).get_text()
        signatures1 = signatures.split()
        ex["# of Signatures"] = signatures1[0]
    
        dataset.writerow(ex)


######Final Step: Now applying all that I've done so far to multiple pages
#the website has 4 pages. 

