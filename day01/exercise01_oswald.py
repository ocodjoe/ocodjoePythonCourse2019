## Fibonacci sequence
## X_[i] = X_[i-1] + X_[i-2], where X_1 = 1, X_2 = 1
## 1,1,2,3,5,8,....

## Write a for loop, while loop, or function (or all three!) to create a
## list of the first 10 numbers of the fibonacci sequence

#answer: I'm creating a loop
#fibonacci = []
#for i in range(1,10):
	#if i < i-1 
	#come back to this

#Here's the correct one:
fibonacci = []
for i in



#"""return true if there is no e in 'word', else false"""
#def has_no_e(word):

#attempt 1:
#def has_no_e(word):
    #for i in "word":
	    #if i != "e":
		#return "TRUE"
#print answer
#has_no_e("word")

#attempt 2:
#def has_no_e(word):
    #if i in "word" == "e":
        #print("TRUE")
    #elif i+1 in "word" =="e":
        #print ("TRUE")
    #elif i+2 in "word" == "e":
        #print ("TRUE")
    #elif i+3 in "word" == "e":
        #print ("TRUE")
    #else:
        #print("FALSE")

#word = "kofi"
#has_no_e(word)

#attempt 3: 
def has_no_e(word):
    for i in range(1, len(word)):
        if i == "e"
        #cont. here...
	

#Here's the correct one:
def has_no_e(word):
    return "e" not in word
[has_e(abcd), has_no_e(abcde)] #this applies to next questio



"""return true if there is e in 'word', else false"""
#def has_e(word): 



"""return true if word1 contains only letters from word2, else false"""
#def uses_only(word1, word2):

#Here's the correct answer:
def uses_only(word1, word2):
    return not False in [i in word2 for i in [j for j in word1]]
[uses_only('abcd', 'abcde'), uses_all('abcd','abcde')]
#this apply to next question


"""return true if word1 uses all the letters in word2, else false"""
#def uses_all(word1, word2):


"""true/false is the word in alphabetical order?"""
#def is_abecedarian(word):
def is_abecedarian(word)  #cont. here. 
