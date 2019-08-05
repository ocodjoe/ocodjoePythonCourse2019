## Trick and explanation of base conversion
## http://www.purplemath.com/modules/base_why.htm

#######QUESTION 1

"""convert positive integer to base 2"""
def binarify(num): 
    #I need to divide num by 2
    remainder = num %2 
    #store quotient and remainder
    num/=2
    #repeat until quotient (i.e. the num) != 0
    while num !=0
        remainder =num%2
    #reverse stored remainders
    #return reversed remainders as string.
    return remainder.reverse()

binarify(20)

#this is the correct one:

def binarify(num):
    remainder = []
    while num !=0:
        remainder.append(str(num % 2))
        num //= 2
    remainder.reverse()
    return ''.join(remainder)

binarify(20)

#Lesson 1: To move from blank to something, start by writing down
#the steps of what you might do. Then start identifying code/
#technology for it. Inspiration may come mid-way. 

#Lesson 2: If you want to test parts of the code in python,
#type python and run it in the terminal. You don't have to
#run the entire script to see what comes up.


######QUESTION 2

"""convert positive integer to a string in any base"""
def int_to_base(num, base):
##steps:
# divide num by base
num//base
# store the numerator
num/=5
# store the remainder
num %5
#repeat first three steps until numerator is 0
while num != 0
    num//= 5
    num %
    
# reverse the remainders
reverse.reminders()
# coerce the remainders as strings
return ''. join (remainder)

#this is the correct one:
def binarify(num,base):
    remainder = []
    while num !=0:
        remainder.append(str(num % base))
        num //= base
    remainder.reverse()
    return ''.join(remainder)

binarify(30,5)


######QUESTION 3

"""take a string-formatted number and its base and return the base-10 integer"""
#def base_to_int(string, base):
# reverse the indices of the list
reverse = string.reverse()
# raise the base to the number corresponding to each index and write them down
base**reverse[0]
# repeat it for everything in the list.
# add each of them together and you have the number in base 10.
sum(thelist)

#So the correct answer is:
def base_to_int(string, base):
    thenumber = len


#"""add two numbers of different bases and return the sum"""
#def flexibase_add(str1, str2, base1, base2):


#"""multiply two numbers of different bases and return the product"""
#def flexibase_multiply(str1, str2, base1, base2):


#"""given an integer, return the Roman numeral version"""
#def romanify(num):

  
# Copyright (c) 2014 Matt Dickenson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.