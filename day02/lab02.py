## Fill in the following methods for the class 'Clock'

class Clock:
  def __init__(self, hour, minutes):
  self.minutes = minutes
  self.hour = hour

    ## Print the time
    def __str__(self):
        return "The time is %d." %(self.minutes)
    ## Add time
    ## Don't return anything
    def __add__(self,minutes):
    
    ## Subtract time
    ## Don't return anything
    def __sub__(self,minutes):
    
    ## Are two times equal?
    def __eq__(self, other):
    
    ## Are two times not equal?
    def __ne__(self, other):






#Lessons: 
#We define the class by giving it an attribute or a name.
#So we create an object (i.e we instantiate) the class so that 
#we can access the things (i.e. the attributes, etc.) inside it. 
#Without instantiation, we can't. 
#A class comes with functions (a.k.a methods) that helps us access the 
#attributes of the class. To make a function for a class you specify the
#keyword self as the first argument (or first of many if there are more
#one arguments). 
#Lesson: To access the attribute(s) of a class you use the dot operator.
#Thus you use instantiation.name_of_attribute()


#Example 1: creating the class and instantiating it. without giving it a name.
class Snake:
    pass
snake=snake()

#Example 2: Creating the class, instantiating it, and giving it an attribute
#Note how you give a name first before you instantiate. 
class  Snake:
    name = "python"
snake = Snake()

#Example 3: Creating the class, instantiating it, giving it an attribute, and
#accessing that attribute using the dot operator
class Snake:
    name = "python"
snake = Snake()
snake.name

#Example 4: Creating the class, instantiating it, giving it an attribute,
#creating a function that changes the attribute's name, instantiating the 
#class, and using the dot operator to use the function to change the attribute
#name of the class. 
class Snake:
    name = "python"
    def change_name(self, new_name): 
        self.name = new_name

snake = Snake()
snake.change_name("anaconda")
print snake.name

#Example 5: Creating the class, giving it an attribute (but using the init 
#function this time around so that it gets the attribute during run time),
#creating a function for changing the attribute's name, and actually using 
#the function to change the attribute's name

class Snake:
    def _init_(self, name):
        self.name = name
        
    def change_name(self, new_name):
        self.name = new_name

python = Snake("python")
anaconda = Snake("anaconda")

print (python.name)
print anaconda.name


