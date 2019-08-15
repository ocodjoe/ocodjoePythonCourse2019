#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 18:41:54 2019

@author: oswaldcodjoe
"""

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
    
    #Extracting the urls of each petition into a list
    address = "https://petitions.whitehouse.gov/#signapetition"
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
        
        