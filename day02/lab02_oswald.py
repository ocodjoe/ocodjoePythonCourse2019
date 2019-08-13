
class Clock:
    def __init__(self, hour, minutes):
        self.minutes = minutes
        self.hour = hour

    ## Print the time
    def __str__(self):
        return "The time is %d:%d." %(self.hour,self.minutes)
    ## Add time
    ## Don't return anything
    def __add__(self,minutes):
        self.minutes += minutes

    
    ## Subtract time
    ## Don't return anything
    def __sub__(self,minutes):
        self.minutes -= minutes
      
    ## Are two times equal?
    def __eq__(self, other):
        if self.minutes == other.minutes:
            return True
        elif self.hour == other.hour:
            return True
        else:
            return False
    
    
    ## Are two times not equal?
    def __ne__(self, other):
        if other == self:
            return False
        else:
            return True
        
        

#Lessons: 


clock1 = Clock(10, 15)
print(clock1)

######Testing first part
Class Clock:
    def _init_(self,hour,minutes):
        self.minutes = minutes+30
        self.hour = hour
    
    def _str_(self):
        return "The time is %d:%d." %(self.hour,self.minutes)
#############
class Clock:
    def __init__(self, hour, minutes):
        self.minutes = minutes
        self.hour = hour

    ## Print the time
    def __str__(self):
        return "The time is %d:%d." %(self.hour,self.minutes)
    ## Add time
    ## Don't return anything
    def __add__(self,minutes):
        self.minutes = self.minutes + minutes
        self.hour = hour
        return "The time is %d:%d." %(self.hour, self.minutes)

clock1=Clock(10,15)
clock1+30
clock1-25

print(clock1)

clock1=Clock(10,15)
print(clock1)
other=Clock(9,25)
print(other)m

clock1==other
clock1!=other

###################################My practice session over class02 notes#####
#Below is a definition/specification of what the Book data type is. Thus
#what makes up the Book data type --thus what attributes make up the Book data
#type. In this case, it consists of 6 attributes/things (title, author, pages,
#theme, price, and is_black). Also note that any of these 6 attributes is either
#a string (eg. author), a number (eg. price), ora Boolean(eg. is_black). These
#are the basic data types in python and we've combined them to make a new 
#data type (i.e. Book)

#Lesson: Note that attributes are parameters. And self.title, for example, 
#says that we want the title of any actual book that we create (an object) to
#be equal to the title that we pass into Book(). So if we create a book(eg. book1)
#using book2=Book("Moby Dick","Asante Peter", 500, "Histort", 15, False), we want
#the title of book2 to be exactly as we've passed/specified in Book(). 

class Book:
    def __init__(self, title, author, pages, theme, price, is_black):
        self.title = title
        self.author = author
        self.pages = pages
        self.theme = theme
        self.price = price
        self.is_black = is_black
    
#Below, we are creating an actual book(book1). We call this instantiation because
#because this an instance of a data type that we've specified/defined above(i.e.
#Book). We can create book2, book3, etc.. all of which will be instances of Book
#class or Book data type.
book1 = Book("French Prince of Belair","Oswald Codjoe", 200, "Fiction", 45, True)
book2 = Book("Moby Dick","Asante Peter", 500, "Histort", 15, False)

#Below, we can manipulate or play around with this actual book (an object)just 
#like we can any of the 3 data types in python. And we can access the attributes
#of this object using the dot operator. 
print(book1.price)
book1.price =50
print(book1.price)
print(book1.is_black)

print(book2.price)

##Lesson: The reason why we have classes is because they make it possible 
#model just about anything (stocks, pens, products, books, people, etc.) in the 
#computer programs that we write.

###################################################3
#Here's an example of practical usage of a class in creating an online quizz.
#specify a class so you can create a question data type
class Questions:
   def __init__(self, question, predetermined_answer):
        self.question = question
        self.predetermined_answer = predetermined_answer

#create an actual question object/a.k.a instantiate the Question class.
question1 = Questions("Who's the current chancellor of Wash U?", "Andrew Martin")
question2 = Questions("What is the offical Wash U color?", "green")

#now create a function that takes the objects question1 or question2 as 
#an argument and: (i) displays it to the user, (ii) records the user's response,
#(iii) and gives the user a grade.

def ask_and_grade(question1): #for now I'm just testing question1
    print(question1.question)
    answer = input()
    grade=0
    if input() == question1.predetermined_answer:
        grade +=1
        print("You scored %s out of %s in this quiz") %(grade, "1")
        
        print("Bravo, you sure know you chancellor!!")
    elif input() != question1.predetermined_answer:
        print("No, the current chancellor is Andrew Martin")
    answer=0
    grade = 
    

ask_and_grade(question1)
####Come back to working on this example later
##############################################

###Lesson: The reason why we include functions(a.k.a methods) into a class
#is so that a user can: (i) get information/attributes about the various objects(a.k.a 
#instantiations) of the class, and (ii) modify information/attributes of various
#objects of the class. Here's an example from the Book class. 

#Define/specify the class
class Book:
    def __init__(self, title, author, pages, theme, price, is_black):
        self.title = title
        self.author = author
        self.pages = pages
        self.theme = theme
        self.price = price
        self.is_black = is_black

#create some objects/instantiations of the class
book1 = Book("French Prince of Belair","Oswald Codjoe", 200, "Fiction", 45, True)
book2 = Book("Moby Dick","Asante Peter", 500, "Histort", 15, False)

#Create a few class functions that you think might be useful. Starting with one
#that tells the user if a particular instantiation/object of the class has
#a price of more than $10. Finaly, note that we call the class functions using
#instantiation.classfunction().

def more_than_10(self):
    if self.price > 10:
        print(True)
    else:
        print(False)

more_than_10(book1)

#This class function tells us whether or not the author's name starts with A
def author_name(self):
    alphabets =[letter for letter in self.author]
    if alphabets[0]=="O":
        print(True)
    else:
        print(False)

author_name(book1)

##Lesson: Just an aside, you can create a class in a .py file separately,
##then import it into your current .py file using from name_of_file, import
#name_of_class. Then you can have access to all the functions/methods,and
#instantiations/objects of the class. 

##Lesson: The idea behind inheritance in classes is to enable a user "borrow"
#functionality(i.e functions/methods) from an existing class for a new
#class without having to copy and paste or specify the functions/methods
#from the "lending" class to the "borrowing" class. Here's an example.

#Here's a book class with 2 functions. 
class Book:
    def __init__(self, title, author, pages, theme, price, is_black):
        self.title = title
        self.author = author
        self.pages = pages
        self.theme = theme
        self.price = price
        self.is_black = is_black
        
    def more_than_10(self):
        if self.price > 10:
            print(True)
        else:
            print(False)
            
    def author_name(self):
        alphabets =[letter for letter in self.author]
        if alphabets[0]=="O":
            print(True)
        else:
            print(False)
                

#Now If I'm making another class that has the same functions and attributes as Book, instead
#of copying and pasting (or writing those functions and attributes all over again), I can 
#simply say (assuming this new class is called Textbooks):

class Textbooks(Book):  #thus inherit all the functions and attributes from Book
    def makeit(self):   #add this function to it
        print("That's it") 

#The code above is saying: take all the functions 
textbook1 = Textbooks("Polisci","Codjoe",240, "comparative", 35, True)

textbook1.price

textbook1.more_than_10()
################################
#Lesson: Polymorphism is a special case of inheritance where the class that
#inheriting the attributes and functions is not a new class per se but a 
#sub class. 

################################
help("modules")  #This lists all the modules currently installed. 

###I'm building a calculator
first_number = int(input("enter first number: "))
operator = input("what operation do you want to perform: ")
second_number = int(input("enter second number: ")) 

if operator == "+":
    print(first_number + second_number)
elif operator == "-":
    print(first_number - second_number)
elif operator == "*":
    print(first_number * second_number)
elif operator == "/":
    print(first_number / second_number)
else:
    print("Sorry, I can't compute your results")

####################################################
####I'm building a translator here
    #I want to take the word from the user
    #I want to take/get the language they want to translate in
    #If the language is not equal to french, I want to tell them I can't translate
    #if the language is equal to french,I want to take the word and put it into
    #some function that generates french translation from the internet.
    
    #Alternatively, I could create a 2 lists of english words and their
    #french translations.
    #So that if the users input is equal to any word in the list, I return
    #the french translation in the other list.
    #If not, I say sorry, can't translate or out of scope of translator.
    
words_english =["boy", "girl", "husband", "wife", "pen"]
words_french = ["garcon", "fille", "mari", "femme", "stylo"]

word = input("What may I translate for you?")

if word == words_english[0]:
    print("The french translation is: " + words_french[0])
elif word == words_english[1]:
    print("The french translation is: " + words_french[1])
elif word == words_english[2]:
    print("The french translation is: " + words_french[2])
else:
    print("Sorry this word is out of my ken")
    
#Alternatively, I can put all these into a function that spits out results

def translator(word):
    
    words_english =["boy", "girl", "husband", "wife", "pen"]
    words_french = ["garcon", "fille", "mari", "femme", "stylo"]
    
    if word == words_english[0]:
        return ("The french translation is: " + words_french[0])
    elif word == words_english[1]:
        print("The french translation is: " + words_french[1])
    elif word == words_english[2]:
        print("The french translation is: " + words_french[2])
    else:
        print("Sorry this word is out of my ken") 
        
        
translator("boy")
translator("husband") 
translator("orange")
    


##--------------------------Exception Handling------------------------------
#I'm trying my hands at exception handling to get an overview of it before
#class starts tommorrow.

##Lesson: The goal of exception handling is to catch errors in our programs
#usually, when a mistake happens in a program, python(i.e. it's interpreter)
#will generate an error message. However, we have to read carefully in order
#to pinpoint what's wrong -- and that can be a drag. Instead, we want to 
#specify our own error message so it's very clear (almost immediately) what
#has gone wrong. And we can specify as many error messages as we like and even
#customize the message to suit the occassion. Here are some examples.

#suppose somewhere in our program we take an input from the user and print
#out a message. But this input has to be a number not string. So we create
#an error message, which will show whenever the user enters the wrong input. 
#We use the try and except commands.

try:
    number = int(input("Enter your exam index number: "))

except: 
    print("You've made an invalid entry.")

#Here's another example that caters for 2 possible errors that the user could
#make -- i.e. not entering an integer and, maybe, entering an indeterminate value.
#So, below, if the mistake is the first, you get the second error message, and if
#it's the second, you get the first error message. 

try: 
    10/0
    number = int(input("Enter your exam index number: "))

except ValueError:
    print("You've made an invalid entry.")

except ZeroDivisionError:
    print("You've entered a non-existent value.") 
    
#come back here and look at types of errors you can except
#. It seems you can't just write anything there. 
    
##Finally, you can store the errors to be excepted as a variable so that
#it prints the variable.
    
try:
    number = int(input("Enter your exam index number: "))
    
except ValueError as thee:
    print(thee)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    