#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 11:25:30 2019

@author: oswaldcodjoe
"""

##So I'm creating 3 classes/modeling 3 things: Portfolio, Stock, and MutualFund.
#Portfolio will be the main class and Cash(maybe), Stock, and MutualFund subclasses.

##Portfolio is defined to the following attributes: Cash, Stock, and Mutual Fund

##Portfolio has the following methods to 'manage/manipulate' its instances:
#addCash(amount) to add cash to it, buyStock(quantity_of_shares, name_of_stock),
#buyMutualFund(quantity_of_shares, name_of_mutualfund), sellStock(quantity_of_
#shares, name_of_stock), sellMutualFund(quantity_of_shares, name_of_mutualfund),
#withdrawCash(amount), history() to print all transactions in order ot time.

##Stock is defined to the following attributes: Price, and Symbol

##Mutual Fund is defined to the following attributes: Symbol 

###-----------------------------------------------------------------------

class Portfolio:
    def __init__(self, Cash, Stock, MutualFund):
        self.Cash = Cash
        self.Stock = Stock
        self.MutualFund = MutualFund
        
    def addCash(self, amount):
        try:
            if type(amount) == int:
                new_amount = int(self.Cash) + amount
                return "You've added $%d. You now have $%d in cash." %(amount, new_amount)
            elif amount < 0:
                new_amount = int(self.Cash) - amount
                return "You've subtracted $%d. You now have $%d in cash." %(amount, new_amount)
            else:
                raise Exception
        except:
            raise ValueError ("Please enter a number, not a string.")
    
            
    def buyStock(self, share_qty, stock):
        #Later on, modify to raise exception if wrong value is entered.
        if share_qty > 0:
            new_qty = self.Stock
            
        return "You've bought %d shares of %s." %(share_qty, stock.Symbol) 
        
    def buyMutualFund(self, share_qty, mutualfund):
        return "You've bought %d shares of %s." %(share_qty, mutualfund)
        
    def sellStock(self, share_qty, mutualfund):
        return "You've sold %d shares of %s." %(share_qty, stock)
        
    def sellMutualFund(self, shares_qty, mutualfund):
        return "You've sold %d share of %s." %(share_qty, mutualfund)
    
    def withdrawCash(self, amount):
        return "You've withdrawn %d." %(amount)
    
    def print(self):
        return self.database
        
    def history(self): 
        return "You've conducted %s so far." %(self)
        
class Stock:
    def __init__(self, Price, Symbol):
        self.Price = Price
        self.Symbol = Symbol
            
class MutualFund:
    def __init__(self, Symbol):
        self.Symbol = Symbol
            
s = Stock(20, "HFH")             #creating stock and 2 mutual funds
mf1 = MutualFund("BRT")
mf2 = MutualFund("GHT")

pfA = Portfolio(Cash = 100, Stock = [20,"HFH"], MutualFund = "BRT" )
print(pfA.MutualFund)
pfA.buyStock(5,s)
pfA.addCash(-50)
print(pfA.db) 



pfA.buyStock(5,s)


###My quick insights from videos so far:
    ##A class can consist of variables too, not just functions.
    ##When accessing components of a class, if the component is a function,
    #you use name_of_class.name_of_function(). But if it's not a function,
    #just use name_of_class.name_of_component. Thus without brackets. 
    
example ={"name":"oswald", "day":20, "year":1990}
print(example)

######My own examples############
#Below, is a class that consists of one variable, name, and 3 methods. The
#last method is used to manipulate the variable, name. 
class Chat:
    name = "Jesse"
    
    def insert(self):
        print("We inserted something")
        
    def delete(self):
        print("We deleted something")
    
    def change(self, value):
        self.name = value
        

c = Chat()
c
d = Chat()
d

c.insert()
c.delete()       
            
c.change("Thomas")
c.name

#####My Lessons from Rpython####################
#The idea behind classes is that we normally have 3 classes (types of) of data: number, string,
#and Logical or Boolean. And we can create several customized classes (types of) data that 
#combine the already existing ones (number, string, logical) that we know. Thus, we 
#can view software as a collection of classes and objects. This makes programming more
#efficient. Thus, we design software using classes and objects. 

class Dog:
    pass       #telling python that I'm not adding any attributes yet.
    
Dog()        #<__main__.Dog at 0x1d38b24cc0> the number at the end is memory address
             #of this instance of the class Dog
Dog()        #Same idea here. <__main__.Dog at 0x1d397917b8>

a=Dog()
b=Dog()

a==b         #The answer (FALSE) shows you that a and b, though of the same class,Dog, are different
             #instances of it. 

type(a)      #The answer shows you that a is an object of class Dog. __main__.Dog

####Building on what we started above.

class Dog:
    
    species = "mammal"  #this is a class attribute that will apply to all objects/instances
                        #thus all dogs of Dogs are mamals.
    def __init__(self, name, age): #the __init__() function assigns, assgins object attributes
        self.name = name  #assigns the name we enter as the name of the object
        self.age = age    #same for age. 
        
philo = Dog("Philo", 5) #the Dog("Philo", 5) runs the function runs __init__()
                        #function in the background, thereby creating philo
mikey = Dog("Mikey", 6) #same idea for Mikey.

philo.name    #we use the dot operator to access the object attributes (i.e. name and age)
philo.age     #same idea for age. 

print("%s is %d and %s is %d." %(philo.name, philo.age, mikey.name, mikey.age))
      #Wohoo... got it. 

#Now, I'm going to check if philo and mikey share the same class attribute.
      
if philo.species == 'mammal':
    print("%s is a %s." %(philo.name, philo.species))

#######Another example, building on top of the one above###############

#If I introduce some new code, I can overwrite the attributes (be they class 
#attributes or instance attributes.) #Here's an example. 
    
class Dog:
    
    species = "mammal"  #this is a class attribute that will apply to all objects/instances
                        #thus all dogs of Dogs are mamals.
    def __init__(self, name, age): #the __init__() function assigns, assgins object attributes
        self.name = name  #assigns the name we enter as the name of the object
        self.age = age    #same for age. 
        
philo = Dog("Philo", 5) #the Dog("Philo", 5) runs the function runs __init__()
                        #function in the background, thereby creating philo
mikey = Dog("Mikey", 6) #same idea for Mikey.

mikey.age = 7       #we change mikey's age to 7
philo.species = "Mouse"     #and change philo's species to mouse. 

print("%s is %d and %s is %d." %(philo.name, philo.age, mikey.name, mikey.age))
      #We see that the age of mikey is changed

if philo.species == 'mammal':
    print("%s is a %s." %(philo.name, philo.species))
    #We see that nothing prints. This is because we've changed the species of philo.
    
#######Another example, duilding on top of what we know so far############
#The idea behind introducing methods/functions into instances/objects is so
#we can access the instance/object attributes, and even manipulate (change/modify)
#them when/if we wish. Here'a an example.

class Dog:
    
    species = "mammal"  #this is a class attribute that will apply to all objects/instances
                        #thus all dogs of Dogs are mamals.
    def __init__(self, name, age): #the __init__() function assigns, assgins object attributes
        self.name = name  #assigns the name we enter as the name of the object
        self.age = age    #same for age. 
    
    def description(self):  #a function that returns the age of the object
        return "%s is %d years old." %(self.name, self.age) 
    
    def speak (self, sound): #a function that takes a sound input and returns
        #a sentence with name and the sound input included. 
        return "%s says %s." %(self.name, sound) 
    
mikey = Dog("Mikey", 7)
print(mikey.description()) #note we use print, otherwise, the sentence won't show
                           #and we input nothing because the function is designed to 
                           #take just 1 element (thus self, which we normally don't
                           #write).  

print(mikey.speak("Gruff gruff!")) #same idea here.  

###############Another example,.##############
print(isinstance(mikey,Dog)) #we use isinstance() function to tell if 
                            #something is an instance of a given class.
print(isinstance(mikey,object)) #and we use the same function to check
                                #something is an object.

dir (mikey) #we use the dir() function to tell us all we can find about 
            #an object (i.e. functions, attributes, etc.) 
type(mikey) #we also use the type() function to tell us 

#Note: python emphasises readability over dry(i.e don't repeat yourself) so
#if inheritance doesn't make sense to you know don't do it. To use inheritance
#look through your classes and see how they are related and see if it's
#possible to build on top of each other or forge some relationship. Only then
#do you use inheritance.  

#Lesson Notes from Rpython on OOP########################
#Object Oriented Programming (OOP) is a style of programming that enables us
#to build programs that manipulate data with efficiency. For example, if I ask
#a kid to design a program that takes his data of birth and calculates and 
#displays his age, he can do so easily because there are few data to keep 
#track of. However, some data manipulation programs involve a lot of different data.
#And to keep track of them we use OOP. Where different data are store and handled
#as objects/things. And we use classes to create objects.



 