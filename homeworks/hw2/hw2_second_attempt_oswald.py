#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 18:41:54 2019

@author: oswaldcodjoe
"""

#Here are my steps:
#1: Click on one petition and use it's url to extract relevant info. to test
  #how it's done.
# 2: Figure out a way to get the urls of all the petitions from the home page, and store
  #them in a list. Or create a for loop such that each petition's url is considered.
# 3: Figure out a way to apply step 1 to each of the urls in the list.
# 4: Final step, figure out a way to way to apply step 1 to each of the
  #urls in each of the 5 home pages containing 20 petitions.  

##Importing all relevant modules
from bs4 import BeautifulSoup
import urllib.request
import re
import csv
import unicodedata 

#Creating a csv file with appropriate headers
with open("petitions_data.csv","w") as f:
    dataset = csv.DictWriter(f, fieldnames = ("Title","Published Date","Issues","# of Signatures"))
    dataset.writeheader() 
    
    #Accessing each of the website's 5 pages that contain petitions
    all_pages = ['page=0','page=1','page=2','page=3','page=4']
    for i in range(0,5):
        addendum = all_pages[i]
        address = 'https://petitions.whitehouse.gov/petitions?%s' %addendum
    
    
        #Extracting the urls of each petition into a list
        page = urllib.request.urlopen(address)
        html_1 = BeautifulSoup(page.read())
        links_a = html_1.find_all('a')
        links_b = links_a[12:51] 
    
        #Opening each url and extracting relevant data into a dictionary
        for i in range(0,39):
            web_address = 'https://petitions.whitehouse.gov/%s' %links_b[i]['href']
   
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
    
            #Transferring the contents of the dictionary into the csv file.
            dataset.writerow(extract) 
        
        