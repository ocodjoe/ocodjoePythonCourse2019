#### Syntax

## Strings ------------------------------------------------

s1 = "hi my name is ryden" ## double quotes

s2 = 'how are you?' ## single quotes

s3 = """ a string can even span
multiple lines""" ## triple quotes

name = "ryden"
age = "26"
intro = "Hi, I'm " + name + ", I'm " + age

## call characters w/in string  
##Lesson: This means selecting/referring to characters
##in a string. Note that in python, indexing starts with 0. 
print(name[0])
print(name[1])
print(name[2])

## strings are immutable, variables can change
## Lesson: Indices in python start with 0. Also, you select from
## right end starting with -1, -2, all the way
name[0] = "a"
name = "nebuchadnezzar"

## splitting strings is useful
##Lesson: If you want to split a word into its component letters you
##use the function [letter for letter in name of object] 
## If you want to split sentence into its component words, you 
##use the function name of object.split() with nothing in the brackets
## If you want to split a sentence into its component phrases,
#you use name of object.split(",") with that "," in the bracket.
with nothing in the bracket 
word_list = intro.split()
print(word_list)

phrase_list = intro.split(",")
print(phrase_list)

letters_list = [letter for letter in name]
print([i for i in name])

## concatenating strings is useful, too
##Lesson: If you want to join strings, you first make an object containing
##the strings and then you use that object as argument in the function
## "".join(), thus if you want no space between the joined strings when they are
#joined. If you want space between the strings when they are joined, you use
## " ".join(). And if you want each of the strings listed on a new line when
##joined, you use "\n".join(). Note that the reason why you first store the
##strings as an object is because "".join(), " ".join(), and "\n".join() can 
## take only one argument so you can't specify all the strings to be joined
## in the bracket.
rename = "".join(letters_list)
print(" ".join(letters_list))
print("\n".join(letters_list)) #this creates a new line for each letter


## Indexing is flexible in python 
## What's happening here?
##Lesson: When the index comes before the colon, it means we are referencing
##everything including and including that index. And when the index comes
## after the colon, it means we are referencing/selecting everything up 
## and including that index. Finally, when you see double colons before
## a positive index, say 3, it means a sequence of every third element
##from the beginning. When its a negative number, say, -3, it means a sequence
## of every third element from the end. 
num_string = "0123456789"
print(num_string[2:]) ## index 2 through end. 
print(num_string[-2:]) ## index -2 through end
print(num_string[:2]) ## up to index 2
print(num_string[:-2]) ## up to index -2 #everything to the last two
print(num_string[::2]) ## sequence, every other
print(num_string[::-2]) ## sequence, every other from the end
print(num_string[::3]) ## sequence, every third from beginning


## Integers ------------------------------------------------
##Lesson: %d is the format character for numbers. And %s is the format 
##character for strings. And %r is also a format character but presents
##stuff just the way you type it in. 

##Lesson: % is for modulars and // gives precise divisions while /gives
#just floor divisions. And ** means squared.

## the usual operators
print(5 + 2)
print(5 - 2)
print(5 * 2)
print(5 ** 2) #this is 5 raised to the power 2. 
print(5 / 2) ## in python2, this is floor division. #This gives you the float (run down)
print(5 // 2) #this gives you the exact value.

whole = 5//3
remainder = 5%3. #this is modular arithmetic
"Five divded by three is %d and %d fifths" % (whole, remainder)

## assignment is flexible
##Lesson: When you see any operator paired with an equal to sign, and there's
## an object on one side and a data element on the other, it's telling python
## to do something to the object and store it as an object of the same name.
##So for example multiply the object 5 by 2 and store it as the object 5.
five = 5
five += 1 #adds 1 and sets five as the new value
print(five)
five /= 3 #divides by 3 and sets five as the new value
print(five)
five -= 1
print(five)
five *= 2
print(five)


## Floats ------------------------------------------------

## Real numbers
## Add decimal to integer
## Be careful with the distinction here!

##Lesson: The function float just takes an integer and turns it to a 
##decimal. The equivalent of turning an integer value to numeric value in R

print(12//5)  #note: float has decimals, others are just integers.
print(12.0/5)
print(float(12)/5)


########CONTINUE HERE. (data structures in python..
##lists, tuples, dictionaries, strings, sets, and frozensets)

## Lists ------------------------------------------------

## A collection of any type of objects -- even lists -- like in R
## Lists will probably be your goto storage in Python, like vectors in R
##Lesson: A list is one of 6 or so data structures in python. It's a collection
##of objects, even other lists. To create a list, open a square bracket, and
## input the items, separating them by a coma. And if you want to add an item
## to a list use the function name_of_list.append(), placing in the bracket
##the item you wish to add. But if you want to add another list to a list, use
##the function name_of_list.extend(), putting in the bracket the list you want
##to add.

cohort = ["Oswald", "Jordan"]
cohort.append("Ryan") ## add one element. #append is for adding a single element
print(cohort)

cohort.extend(["Ben", "Crystal"]) ## add a list. #extend is for adding another list
print(cohort)

## NOT like this...
#cohort = cohort.append()
##Lesson: the function len() gives you number of items in the list

## remember our indexing... starts at 0!!
print(cohort[0]) ## first
print(cohort[-1]) ## last.  #just note -1 means last element, -5 means fifth to last element, and so on.
print(cohort[len(cohort)]) ## !!!

##Lesson: Indexing in python starts from 0. Also, if you want to add
##an item to a list, you use the name_of_list.insert() function, specifying
##in the bracket the index where you want the item placed, and the item.
##And if you want to delete an item from a list, you use the 
##name_of_list.pop() function, specifying the index of the item you want
##removed in the bracket. If you don't specify anything, the last item
##in the list will be removed/deleted. 
## lists are mutable
cohort[0] = "Alexandra" 
print(cohort)

## Insert by index
cohort.insert(2, "Lucas")
print(cohort)

## Remove, but be careful
last_element = cohort.pop()  #so cohort.pop just elimnates the last element?
print(cohort)
print(last_element)

third_element = cohort.pop(2)
print(cohort)

list_of_lists = [cohort, ["JB", "Ryden", "David", "Erin"]]
print(list_of_lists)



## Tuples ------------------------------------------------
#Note: We use a tuple when we want to make a list such that no one can change it's elements.
## Like lists, but immutable
## Not super common....
##Lesson: A tuple is a list that cannot be edited. Thus, its components 
##cannot be changed. You make a tuple by placing its components into 
##round brackets -- unlike square brackets for lists. 
##everything else about appending, popping, inserting by index and 
##selecting/referring to components is impossible. 

tup = (1,6,5, "Apple", ["python", "R"]) #note: to make a tuple, you use a curly bracket. but square bracket for list.
print(tup[1])

tup[1] = 10000 ## !!!

tup.append(10000) ## !!!



## Dictionary ------------------------------------------------

## Like a list, but two key differences:
## - elements not ordered
## - elements are named with keys
## Therefore, you have to index with key names
## 
## Dictionaries are super useful!
##Lesson: A dictionary is a list whose elements are not ordered and are
##named with key. It's the python equivalent of a dataframe with named 
##columns. So you select the elements using the key names.
##If you want to create a dictionary open a curly bracket and enter the 
##key name in quotes, followed by a colon, and followed by the value
##corresponding to the key name in quote, then a comma, then another key, etc.
##If you want to get the key names of a dictionary, you use the function
##name_of_object.keys(). And if you want to get the values of a dictionary,
##you use the function name_of_object.values().
##If you want to select/refer to a particular key you use name_of_object[], 
##specifying in quotes in the square bracket the key name.
##And if you want to replace or edit a value in a dictionary, you select it and
##then you assign the new value. 

ryden_info = {"name" : "Ryden", "age" : 26, "research" : ["social media", "methods"]}

print(ryden_info.keys()) #this is like colnames in R
print(ryden_info.values()) #gives the values

ryden_info[0] ##!!!
ryden_info["research"] #so you index using the keys not indices as we know them. That's why we say it's not ordered

ryden_info["last_name"] = "Butler"
print(ryden_info)





## Booleans and Conditionals ------------------------------------------------
##Lesson: = is an assignment operator while == is a comparison operator
##which means equal to. != is also a comparison operator, which means not 
##equal to. 
 which means not equal to. 
t = True
f = False 
print(t == f) #
print(t != f) #not equal


## Perform operation(s) if condition is met 
##Lesson you can use (and you normally do use) conditions in functions
##thus as the underlying code in functions. Also, don't forget your colons
##and indentations -- without these, your code won't run. It's a syntax
##issue. You want to leave 4 spaces to make an indent. So usually it's def 
##function then colon, then new line then four spaces then the conditionals.
##With the conditionals if then condition then colon, then newline then 4 spaces
#then return (whatever value). Then next line (this has to have the same
##indentation as the if) and so on.
##Note that we use if, elif (which means else if) and else to make conditional
##operations in python -- actually, most languages in general. 
x = 2
if x == 1:
	print("x is one")
elif x == 2:
	print("x is two")        #note: elif means else if.
else:
	print("x is neither one or two")

if x == 2 or x == 3:
	print("Yay!")

if x == 2 and x < 5:
	print("Yay!")

## Note: indentation matters in python, but ipython can help
x = 2
if x == 1:
          print("x is one")

#########This was my practice example--------------------------
def myfun(x):
    if x==0:
        return (x+5)
    elif x==1:
	    return (x*1000)
    else:
        return (x+20)
##########################--------------------------------------



## Loops ------------------------------------------------ 
##Lesson: We also use loops (for loops and while loops) in functions (usually).
##Again, the rules of indentation and colon still apply.
##Lesson, we use the function range() to generate numbers. And in the round
##bracket, you specify the starting number and ending number. You can also
##specify the increments, if you like. So you have range(1,100,3) meaning python
##should generate numbers starting from 1 with increments of 3, all the way 
##to 100 if possible. 

even_nums = []
for i in range(1,10):     #essentially we are populating even-nums with even numbers.
	if i%2 == 0:
		even_nums.append(i)

hi = []
for i in "hello":          #essentially we are taking each character in hello and populating hi with it
	hi.append(i)

## more succinct way to write simple loop
bye = [i for i in "goodbye"]          #this is the more efficient/pythonic way of doing loops. eg. those above.


while len(even_nums) > 1:         #note: a while loop is just a loop that keeps running as long as some condition is met.
	print(even_nums.pop())    #so when doing a while loop, make sure there's some condition that will trigger a false

print(even_nums)                  #else your loop will run forever. 


#######Here's my example 1:
def myfun(x):
    set = []
    for i in x:
        set.append(i)
    return (set)
    
######Here's my example 2: 
def myfun(x):
    set = [i for i in x]  
    return set

##Note that in these examples, x is just a place holder and depending on your
##code for the function, it will have to be a string or number etc. 
        
########Here's my example 3: 
def myfun(x):
    while len(x) > 1 :
        print x.pop()
    return x.pop()

## Functions ------------------------------------------------

## Write cleaner code
## Allow for easy testing
## Allow for easier trouble-shooting
##Lesson: the indentation (4 spaces thing) and colons still works here
##as they did for the conditionals
## Input, output
def add_squares(x, y):
	return x**2 + y**2

print(add_squares(3,4))
print(add_squares(2,2))



