## Class 08 - Recursion & Sorting

# Search Algorithms

## returns element if it is in the list
def linear_search(mylist, element):
  steps = 0
  for item in mylist:
    steps += 1
    if item == element:
      print(steps)
      return item
  print(steps)
  return None

mylist = range(26)

linear_search(mylist, 1)
linear_search(mylist, 5)
linear_search(mylist, 30)

## returns element if it is in sorted list
def binary_search(sorted_list, element):
  print("Input list is {0}".format(sorted_list))
  print("Input size is {0}".format(len(sorted_list)))
  middle = len(sorted_list)//2
  median = sorted_list[middle]
  if len(sorted_list) <= 1:
    if element == median:
      return median
    else:
      return None
  if element < median:
    left = sorted_list[0:middle]
    return binary_search(left, element)
  else: 
    right = sorted_list[middle:]
    return binary_search(right, element)

mylist = range(1000)
binary_search(mylist, 70)



## Find n'th number in fibonacci sequence
def fib(n):
  if n<=1:
    return n
  return fib(n-1) + fib(n-2)

# fib(8) = fib(7) + fib(6) = 21
# fib(7) = fib(6) + fib(5) = 13
# fib(6) = fib(5) + fib(4) = 8
# fib(5) = fib(4) + fib(3) = 5
# fib(4) = fib(3) + fib(2) = 3
# fib(3) = fib(2) + fib(1) = 2
# fib(2) = fib(1) + fib(0) = 1
# fib(1) = 1
# fib(0) = 0 

for i in range(35):
  print("{0} : {1}".format(i, fib(i)))



# Exercise:

def factorial(n):
##if base case:
##  return something
##else:
##  return a recursive call

##My answer#######
def factorial(n):
    if n==0:
        return 1
    else: 
        return factorial(n-1)*n
    
factorial(2)

##This, above, is a great example of writing functions/coding recursivelly. 
#Thus the algorithimic way of writing 5! is 5*4!.



# Sorting or shuffling

my_numbers = [1, 9, 8, 5, 4, 6, 0, 2, 3, 7] 

#####################################
import random
my_numbers = [1,9,8,5,4,6,0,2,3,7]
random.shuffle(my_numbers)
print(my_numbers) 
#####################################

# Bogo Sort
# 1) Randomize number order
# 2) If sorted: stop; else: repeat

def bogo_sort(numbers):
    random.shuffle(numbers)
    gold_standard = sorted(numbers)
    if numbers == gold_standard:
        return numbers
    else:
        return bogo_sort(numbers)

bogo_sort(my_numbers)

# Selection Sort
# 1) Find minimum of the unsorted list
# 2) Remove minimum and place it in first element on new list
# 3) Repeat until unsorted list is empty

my_numbers = [1, 9, 8, 5, 4, 6, 0, 2, 3, 7]

import numpy 
numpy.argmin(my_numbers)  #note: min is the actual small number in the list
                          #and argmin is the smallest indext.

def selection_sort(numbers):
    new_my_numbers = []
    while len(numbers) > 0:
        new_my_numbers.append(numpy.min(numbers))
        numbers.remove (min(numbers))
    return new_my_numbers

selection_sort(my_numbers) 

# Insertion Sort
# 1) Start with the element in the second position
# 2) Insert it to the correct position to the left
# - Check left-most element until value is greater
# 3) Continue to next position

def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        for j in range(i):
           if numbers[i] < numbers[j]:
               to_insert = numbers.pop(i)
               numbers.insert(j, to_insert)
               print(numbers)

insertion_sort(my_numbers)

# Bubble Sort
# 1) Compare first two contiguous elements, swap if necessary
# 2) Compare next two contiguous elements, swap if necessary
# 3) Continue until end of list
# 4) If swaps occurred in 1 - 3, repeat for first n - 1 elements

def bubble_sort(numbers):
    n = 1
    did_swap = True
    while did_swap == True:
        n_swaps = 0
        for in in range (len(numbers) -1): #come back and check here. 
        
            if numbers[i] > numbers [i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]  #this is how you swap.
                print(numbers)
                if n_swaps == 0:
                    did_swap = False
                else:
                    n += 1
                return numbers
            
    

#Note: the difference between return and print is print returns the answer for each
#iteration but return just returns the answer for the final iteration. 

#Below is an exmaple of swapping: 
x=10
y=20
x,y = y,x

print(x)
print(y)
################3


# Plotting

pip install matplotlib

import matplotlib.pyplot as plt

x = range(1, 101) ## # of elements in list
y = range(1, 101) ## time
plt.subplots_adjust(left = .13, right = .95, top = .9, bottom = .3)
plt.plot(x, y)
plt.legend(['hi', 'bye'], loc = "upper left", prop = {"size":10})
plt.ylabel("Y")
plt.xlabel("X")
plt.title("The Effect of Different Sort Algorithms on Runtime")
txt = """
Maybe a description here
"""
plt.figtext(.5, .05, txt, fontsize = 10, ha = "center")
plt.savefig('plot.pdf') 

####################################
#Note: The way to get time is: You can find help online too.  
import time
start_time = time.time()
main()
print('------%s seconds ------' %(time.time()-start_time)) 




###############################
def insertion_sort(numbers): 
    return answer