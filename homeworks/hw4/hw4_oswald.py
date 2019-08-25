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




