# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

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
print(other)

clock1==other
clock1!=other