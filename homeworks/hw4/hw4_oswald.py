#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 21:30:03 2019

@author: oswaldcodjoe
"""

#insertion sort
#The idea is to start from the second item in the list, look at the item to the left of it,
# and check if the item to the right of this item is greater than or less than it.
#if it's greater swap (bring this item to the left of the other item). The check again
#if this new item you've just placed to the left of the other is greater/less than the
#item to its left....coontinue till you reach the left most (i.e. beginning) of the list
#If you find that the item to the left of a newly 'inserted/swapped' item is less than
#the item, simply stop the iteration and move to the fourth item in the list
#checking again... like we've done before.  
##It's not the most efficient if you have a large number of items to sort (10k or more). 
#This is in part because it uses nested loops (loops within loops).  
def insertion_sort(A):
    for i in range(1, len(A)): #outer loop
        for j in range(i-1,0,-1): #inner loop
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j] 
            else:
                break
            print (A) 
                
insertion_sort([1,8,9,7,4,3,1,2])
#

#selection sort 
#The idea is to look through the list (from left to right), identify a minimum
#value and then move that minimum value to the front of the list (i.e. the leftmost)
#position in the list or before/after the number in that position depending on 
#whather it's greater or less than it. 
#Again, it's inefficient when you have 10k or more to sort cos of nested loop
def selection_sort(A):
    for i in range(0, len(A)-1):
        minIndex = i
        for j in range(i+1,len(A)): #unsorted part of list
            if A[j] < A[minIndex]:
                minIndex = j
        if minIndex != i:
            A[i], A[minIndex] = A[minIndex], A[i] 
        print (A)
         


selection_sort([1,8,9,7,4,3,1,2]) 


#Bubble sort
#The idea is to compare the first two items in the list. If one is greater than
#the other, place the smaller one before the greater one. Then move to the next two
#items in the list, and do the same as above (so for example, 1st and 2nd, 2nd and 3rd
#3rd and 4th, etc.). Go on until you've finished the entire list
#Again, it can also be inefficient like those above.  

def bubble_sort(A):
    for i in range(0, len(A)-1):
        for j in range(0, len(A)-1-i): #because the ith item in the list has been sorted already
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
            print (A)
            
bubble_sort([1,8,9,7,4,3,1,2])    


##Bogo sort
#

#####################Now Checking the time it takes to execute#################

##Aside: learning to create a list of randomly shuffled itmes. This helps me
#create a random list of n numbers to be sorted. And I can use this to test my 
#sorting algorithms  and how long they take to execute for different lengths of the list.

import random
numbers = []
for i in range(0,5):
    numbers.append(i)
random.shuffle(numbers)
#print(numbers) 
########################################3
import time
start = time.time()

selection_sort(numbers)

end = time.time()
print (end - start)

y1 = 0.0002498626708984375 #This is how long it takes to do solection sort with n=5

###Now trying for when n=10
numbers = []
for i in range(0,10):
    numbers.append(i)
random.shuffle(numbers)
#print(numbers) 

start = time.time()

selection_sort(numbers)

end = time.time()
print (end - start)

y2 = 0.0015039443969726562 #This is how long it takes when n=10

####Now trying when n=15
numbers = []
for i in range(0,15):
    numbers.append(i)
random.shuffle(numbers)
#print(numbers) 

start = time.time()

selection_sort(numbers)

end = time.time()
print (end - start)

y3 = 0.0005471706390380859

###Now trying for when n=20
numbers = []
for i in range(0,20):
    numbers.append(i)
random.shuffle(numbers)
#print(numbers) 

start = time.time()

selection_sort(numbers)

end = time.time()
print (end - start)

y4 = 0.0005292892456054688

###Now trying for when n=25
numbers = []
for i in range(0,25):
    numbers.append(i)
random.shuffle(numbers)

start = time.time()

selection_sort(numbers)

end = time.time()
print (end - start)

y5 = 0.003922939300537109


######Notes for getting time complexity of codes in python
###It's helpful to always think of the square farm and weeding it analogy. Weeding
#time increases with area, not just one side or the other. 

##Identify the time complexities for each of the individual components of the body
#of code and add them.
## During addition, drop constants. For example, O(n) + O(2n) is still O(n) 
##Different inputs means different variables. for example, when a python function
#has a nested loop (eg. one loop inside another and the list on which is loop
#is performed is different) the time complexity is O(a*b) where a and b are the 
#respective lengths of the lists. Of course if the lists have the same length,
#then time complexity is O(a^2) or whatever.
##When adding, drop non-dominant terms. Example, if you have O(n) + O(n^2) the answer
#is O(n^2). We just want to have some idea of how it's going. hence, such a focus.





