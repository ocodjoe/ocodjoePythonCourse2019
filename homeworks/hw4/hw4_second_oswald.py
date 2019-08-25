#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 12:02:52 2019

@author: oswaldcodjoe
"""

#This is a bubble sort algorithm of time complexity O(n^2)
def bubble_sort(A):
    for i in range(0, len(A)-1):
        for j in range(0, len(A)-1-i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
            print (A)
            
#This is a random list generator for when len(A) = 2
import random
A = []
for i in range(0,2):
    A.append(i)
random.shuffle(A)


#This calculates the time it takes to run bubble_sort(A) when len(A)=2
import time
start = time.time()

bubble_sort(A)

end = time.time()
print(end - start)

x1=2 
y1=0.0007369518280029297

#This calculates the time it takes to run bubble_sort(A) when len(A)=4
A = []
for i in range(0,4):
    A.append(i)
random.shuffle(A)

start = time.time()

bubble_sort(A)

end = time.time()
print(end - start)

x2=4
y2 = 0.000270843505859375

#This calculates the time it takes to run bubble_sort(A) when len(A) = 6
A = []
for i in range(0,6):
    A.append(i)
random.shuffle(A)

start = time.time()

bubble_sort(A)

end = time.time()
print(end - start)

x3 = 6
y3 = 0.0006749629974365234

#This calculates the time it takes to run bubble_sort(A) when len(A) = 8
A = []
for i in range(0,8):
    A.append(i)
random.shuffle(A)

start = time.time()

bubble_sort(A)

end = time.time()
print(end - start)

x4 = 8
y4 = 0.0006999969482421875

#This calculates the time it takes to run bubble_sort(A) when len(A)=10
A = []
for i in range(0,10):
    A.append(i)
random.shuffle(A)

start = time.time()

bubble_sort(A)

end = time.time()
print(end - start)

x5 = 10
y5 = 0.005377769470214844

##This plots the time complexity of bubble_sort(A)
pip install matplotlib

import matplotlib.pyplot as plt

x = (2,4,6,8,10) ## # of elements in list
y = (0.0007369518280029297,0.000270843505859375,0.0006749629974365234,0.0006999969482421875,0.005377769470214844 ) ## time
plt.subplots_adjust(left = .13, right = .95, top = .9, bottom = .3)
plt.plot(x, y)
#plt.legend(['hi', 'bye'], loc = "upper left", prop = {"size":10})
plt.ylabel("Time")
plt.xlabel("Length of List")
plt.title("The Effect of Different Sort Algorithms on Runtime")
txt = """
Plot 1: How runtime of bubble_sort(A) changes with length of list. 
"""
plt.figtext(.5, .05, txt, fontsize = 10, ha = "center")
plt.savefig('plot1.pdf') 

##################################PART TWO ###################################

#cont. here.. choose different algorithm (of different O() and then do the same as above







