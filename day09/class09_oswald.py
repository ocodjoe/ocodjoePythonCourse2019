#### Class 09
#### Some old and some new data types and tricks 
##The goal here to to go over some of the things we may have seen in passing. Overview. 

#pip install pandas
#pip install numpy
import pandas as pd
import numpy as np

## Pandas ----------------------------------------------------

## like a normal list  #Oh so this is how you make a list 
x = pd.Series([10, 100, 12, 5])
x[0]

## now columns and rows
## input can be lots of things
dt = { 'A' : 1.2, 'B' : [1,2,3], "C" : "hi"} #creates a dictionary
#Note that for A, 1.2 appears on all 3 rows, while for B, 1 on first row, 2 on second,
#and 3 on third. 
df_dictionary = pd.DataFrame(dt, columns = ["A", "B", "C"]) #uses dictionary to make dataframe
df_dictionary 
df_dictionary.dtypes   


l = [[1,2,3], [3,4,5], [7,8,9]]
df_lists = pd.DataFrame(l, columns = ["A", "B", "C"])
df_lists.index ## row names 
df_lists.rename(index = {0:"One", 1:"Two", 2:"Three"})  #this renames the rows. 

ar = np.random.randn(6,4) #this creates a 6x4 matrix whose components are random
df_array = pd.DataFrame(ar, columns = ["A", "B", "C", "D"])
#Note: An array and list are the same idea. The only difference is in how
#you construct them, and the types of operations you can perform on them.


## helpful commands

df_array.head()   #this gives the head like head of dataframe in R
df_array.head(2)  #this gives first two rows
df_array.tail()   #htis gives tail like tail in R

df_array.columns  #this gives the columns

df_array.describe()  #this gives a descriptive summary like summary() does in R

df_array.sort_values(by = "A") 



## indexing

df = df_array

df["A"] ## column A

df["A"][0] ## column then row

df[0:4] ## first 4 rows

df.loc[:,["C"]] ## uses labels

df.loc[1:3,["C"]]

df.iloc[1:3, 1:3] ## uses integer positions

df.iloc[1:2, 1:2]

#Aside: It seems to me that when using a system function, you do function() but
#when using a "class" function, you use object.function().  

df.at[1,"A"] #this prints row 1 of column A

# also
my_data = pd.read_csv('test_csvfields.csv')
my_data

## and a lot more.....



## Tuples ----------------------------------------------------


## Tuples are immutable

my_tuple = (1,'b',3,'d',5,'b')   
my_tuple[1] = {'b':2} #this is trying to change b to 2 but it can't work.
my_tuple[0] ## element at index  0
my_tuple.index('b') ## Gives the index of 'b' - only the first occurence!
my_tuple.count('b') ## Gives the number of times 'b' occurs 

## Lists ----------------------------------------------------


my_square_list=[]
for i in range(0,10):
	my_square_list.append(i**2)
my_square_list

## one line loop!
my_square_list = [i**2 for i in range(10)]
my_square_list

## map is like apply in R #Note: apply() in R is a function that allows us to
#apply another function to elements in a vector, matrix, dataframe, array, etc. 
#quickly and simultaneouly. To do so we write: apply(object, dimension, function).
#So, for example, if I want to apply mean to every row in a dataframe called A,
#I'll specify apply(A,1,mean). If both row and col, apply(A, 1:2, mean). If just
#col apply(A, 2, mean). 

## lambda creates an anonymous function
my_square_list = map(lambda x: x**2, range(0,10))
list(my_square_list)
## like in R...
## sapply(0:9, function(x) x^2)

## another way
def sqr(x): return x**2

map(sqr, range(0,10))
list(map(sqr, range(0,10)))

## zip makes list of item-wise tuples    #come back to this... didn't really understand.
my_list = range(0,10)
zipped = zip(my_list, my_square_list, map(lambda x: x**3, range(0,10)))
zipped
list(zipped)

unzipped = zip(*zipped)
unzipped 
list(unzipped) 

## filter
## returns elements only for which condition is True
filter(lambda x: x == 1, [1,2,3])
list(filter(lambda x: x == 1, [1,2,3]))

filter(lambda x: x < 0, range(-5, 5))
list(filter(lambda x: x < 0, range(-5, 5))) #this uses lambda to create a function
#that returns anything less than 0 and applies it to numbers from -5 to 5.


## .index and .count methods work the same as above

x = [3,6,1,2,8,3,5,7] 

# watch out for assignment
x = x.reverse()

x.reverse() 
x
x[2]
x
x.sort() 
x
x.append([10, 12, 14]) #Oh I see: this just adds a list to the list
x
x.extend([11, 12, 14]) #And this adds the numbers 11, 12, 14 to the existing list
x
x.insert(1,'+') #this says insert the plus sign after 1
x
x.remove('+')  #Removes the first occurence '+'
x
x.remove(3)
x  


## enumerate  #it gives us the index and the corresponding number. 

import string #this imports the string module 

y = [3,1,2,5,2]
enumerate(y) #this gives the indices of the items in the list y
list(enumerate(y)) #this prints out the items plus their indices.

letters = list(string.ascii_lowercase)
letters

## each item is a tuple
for item in enumerate(letters):
	print(item)

## iterate with elements of tuple
for number, letter in enumerate(letters):
	print("%s is the letter with index %s" %(letter,number))
#Interesting: we could have, in the above, used for i, j in enumerate(letters).
#so i, j or number, letter are just place holders that stand for pairs in enumerate(
#letters). 

## more generally, iterate like this with any tuple
for a,b,c in [(1, 2, 3), (10,11,12)]:
	print(a)
	print(b)
	print(c) 


#cont. here...
## Dictionary ---------------------------------------------------- 
#Note: Just an aside, there are now ordered dictionaries too... just fyi. 

zip(letters,range(1,27))
d = dict(zip(letters,range(1,27)))
d

d['a']
d.keys() #Don't expect order! #this prints the keys.
d.values() #this prints the values
d.items() #this prints both the keys and the values


for key, value in d.items():
	if value == 1:
		print(key)


for k, v in d.items():
	print("%s is the letter number %s" %(k, v))

newletter = {'A': 27}
d.update(newletter)   #Oh this updates the dictionary. 

new_a_value = {'a':'first'}
d.update(new_a_value) ## overwrites
d['z'] = 'last' ## overwrites

d["A"].append("hi") 
u = {"A" : [29, 30, 27]}
d.update(u) 


## Tree ----------------------------------------------------
## Our own data structure!
##To help you understand: the data frame analogy. So this below is like what happens
##behind the scenes when you add column or add row or manipulate a data frame in general.
##someone behind the scenes had written this below -- so to speak. So the child is the
##addition and the parent is the data frame and the existing children are the rows or
##columns already in the data frame. 

class Node():
	def __init__(self, value = None):
		self.value = value
		self.parent = None
		self.children = [None, None]			
		
	def __repr__(self):
		return "Node object with value %s" %(self.value)
		
	def __str__(self):
		if self.children != (None,None):
			return "Node value: %s \n left child: \n %s \n right child: \n %s" %(self.value,self.children[0],self.children[1])
		else: return "Node value: %s" % self.value	



class Tree():
	def __init__(self, root=None):
		self.root = root
		self.branches = [[root]]
		
	def add_branch(self, node, children):
		node.children = children
		for branch in self.branches:
			if branch[-1] == node:
				newbranch = branch + [children[0]]
				newbranch2 = branch + [children[1]]
				self.branches.append(newbranch)
				self.branches.append(newbranch2)
				self.branches.remove(branch)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

repr(node1)

mytree = Tree(node1)
mytree.branches
mytree.add_branch(node1,[node2,node3])
mytree.add_branch(node2,[node4,node5])



