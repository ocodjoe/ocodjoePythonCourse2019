## Write a function that counts how many vowels are in a word
## Raise a TypeError with an informative message if 'word' is passed as an integer
## When done, run the test file in the terminal and see your results.
#def count_vowels(word):
    #take the word 
    #specify a list of vowels
    #compare each of the alphabets in the word with the list of vowels
    #create an empty list to be populated with result from below
    #if an alphabet in the word matches with a vowel in the list of vowels --
    #put it into the empty list
    #find the length of the empty (i.e. now populated) list. 
    
#def count_vowels(word):
    #vowels = ["A","a","E","e","I","i","O","o","U","u","Y","y"]
    #answer = []
    #for i in word:
        #if i in vowels:
            #answer.append(i)
    #return len(answer)
            

#count_vowels("evening")
#count_vowels("Peter")


##Now I'm incorporating a TypeError into the function.
def count_vowels(word):
    try:
        word.upper()
        vowels = ["A","a","E","e","I","i","O","o","U","u","Y","y"]
        answer = []
        word2 = [letter for letter in word]
        for i in word2:
            if i in vowels:
                answer.append(i)

        return len(answer)
    
    except:
        raise TypeError("You've entered a non-string. Please enter a word.") 
        
           
    
#count_vowels("Oswald")
#count_vowels(4)
#count_vowels([1,2,3])
##Now I have to run the test file in terminal to see my results. 
#I was using the terminal to open stuff and I had some indentation errors
#so I need to go back to that  and fix before I can run the files.


dir("oswald") #note: this lists all the operations you can perform on oswald


###Notes: So it would have been better to write a function that takes into
#account the lists argument. That way, it can pass all the components of the
#test. And we wouldn't have had to insert something that disqualifies lists. 