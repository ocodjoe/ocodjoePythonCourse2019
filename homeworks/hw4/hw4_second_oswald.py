#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 12:02:52 2019

@author: oswaldcodjoe
"""

#This is a bubble sort algorithm of time complexity O(n^2). Let a be the
#number of operations done in outer loop and b be the number of operations
#done in the inner loop. Since a = b = n = the number of elements in the list,
#this makes the bubble sort algorithm one of time complexity O(a*b) = O(n*n) =
#O(n^2).  
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
##This is a merge sort algorithm of time complexity 0(nlogn), where logn is 
#the number of merge steps, and n is the number of operations done per merge
#step -- and also the number of items in the input/list.

#Creating a merge function to be used in the merge_sort function
def merge(a,b):
    c = []
    a_index = 0
    b_index = 0
    while a_index < len(a) and b_index < len(b):
        if a[a_index] < b[b_index]:
            c.append(a[a_index])
            a_index +=1
        else:
            c.append(b[b_index])
            b_index +=1
    if a_index == len(a):
        c.extend(b[b_index:])
    else:
        c.extend(a[a_index:])
    return c
    
#Testing the merge function
a = [1,3,5]
b = [2,4,6] 

merge(a,b) 

#Creating a merge_sort function that uses the merge function above.
def merge_sort(a):
    if len(a) <=1:
        return a
    left = merge_sort(a[:len(a)//2])
    right = merge_sort(a[len(a)//2:])
    return merge(left,right)

#Testing the merge_sort function
merge_sort([5,4,3,7,9])


#Identifying time complexity of merge_sort when n = 2

import random
Q = []
for i in range(0,2):
    Q.append(i)
random.shuffle(Q)

start = time.time()

merge_sort(Q)

end = time.time()

print (end - start)

x1 = 2,
y1 = 0.00010967254638671875

#Identifying time complexity of merge_sort when n = 4
Q = []
for i in range(0,4):
    Q.append(i)
random.shuffle(Q)

start = time.time()

merge_sort(Q)

end = time.time()

print (end - start)

x2 = 4
y2 = 4.9114227294921875e-05

#Identifying time complexity of merge_sort when n = 6
Q = []
for i in range(0,6):
    Q.append(i)
random.shuffle(Q)

start = time.time()

merge_sort(Q)

end = time.time()

print (end - start)

x3 = 6
y3 = 6.103515625e-05

#Identifying time complexity of merge_sort when n = 8
Q = []
for i in range(0,8):
    Q.append(i)
random.shuffle(Q)

start = time.time()

merge_sort(Q)

end = time.time()

print (end - start)

x4 = 8
y4 = 8.416175842285156e-05

#Identifying time complexity of merge_sort when n = 10
Q = []
for i in range(0,10):
    Q.append(i)
random.shuffle(Q)

start = time.time()

merge_sort(Q)

end = time.time()

print (end - start)

x5 = 10
y5 = 6.008148193359375e-05

#This plots the complexity of merge_sort(Q)

import matplotlib.pyplot as plt

x = (2,4,6,8,10) ## # of elements in list
y = (0.00010967254638671875, 4.9114227294921875e-05, 6.103515625e-05, 8.416175842285156e-05, 6.008148193359375e-05 ) ## time
plt.subplots_adjust(left = .13, right = .95, top = .9, bottom = .3)
plt.plot(x, y)
#plt.legend(['hi', 'bye'], loc = "upper left", prop = {"size":10})
plt.ylabel("Time")
plt.xlabel("Length of List")
plt.title("The Effect of Different Sort Algorithms on Runtime")
txt = """
Plot 1: How runtime of merge_sort(A) changes with length of list. 
"""
plt.figtext(.5, .05, txt, fontsize = 10, ha = "center") 
plt.savefig('plot2.pdf') 
