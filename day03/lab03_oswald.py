import string
## 1. write tests in lab03_tests.py
## 2. then code for the following functions

## Raising errors is more common when developing ------------------------

## These functions all take a single string as an argument.
## Presumably your code won't work for an int
## raise a built-in (or custom!) exception if fed an int


## make all characters capitalized
def shout(txt):
    try:
        result = txt.upper()
        return result 
    except:
        raise TypeError("Please enter a word, not a number.")
            
## reverse all characters in string
def reverse(txt):
    result1 = [letter for letter in txt]
    answer2 = result1[::-1]
    answer3 = "".join(answer2)
    return answer3
#Another way....
    #return txt[::-1]

## reverse word order in string
def reversewords(txt):
    return txt.split()[::-1]

## reverses letters in each word
def reversewordletters(txt):
    return ' '.join([reverse(i) for i in txt.split()])
    

## change text to piglatin.. google it! 
#def piglatin(txt):
#find first vowel
    #one = txt.split()
    #vowels = ["a","e","i","o","u","y"]
    #cont. here later
#Split word on first vowel
#Append characters to left of first vowel to the back of the word
#Append "ay" to the back of the word. 


## Try/catch is more common when using
## someone else's code, scraping, etc. -----------------------------------

## Loop over this string and apply the reverse() function.
## Should throw errors if your exceptions are being raised!
## Write a try/catch to handle this.
 
#string_list = ["hi", "hello there", 5, "hope this works", 100, "will it?"]

#dir("oswald")
#upper("oswald")

#reverse("oswald")

#shout("oswald")	
			
			
			
			

