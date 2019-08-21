## Exercise 1
## Write a function using recursion to calculate the greatest common divisor of two numbers 
## Helpful link:
## https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
def gcd(x, y):
    if x%2 ==0 and y%2 == 0 and x<y:
        return x
    elif x%2 == 0 and y%2==0 and x>y:
        return y
    elif x%2 !=0 and y%2 !=0 and x<y:
        return x
    elif x%2 !=0 and y%2 !=0 and x>y:
        return y
    elif x%2 !=0 and y%2 !=0 and x>y and x%y ==0:
        return y
    elif x%2 !=0 and y%2 !=0 and x<y and y%x ==0:
        return x
    elif x%2 !=0 and y%2 == 0:
        return 1
    elif x%2 ==0 and y%2 !=0:
        return 1
    else:
        return "Sorry, can't calculate"
    
gcd(121,5)  
####################################
##correct answer:
def gcd(x,y):
    while x!=0 and y != 0:
        Q = x//y
        R = x%y
        x=y
        y=R
    if x == 0:
        return y
    if y == 0:
        return x 


gcd(270,192)

### recursive approach

def gcd2(x,y):
    if x ==0:
        return y
    if y == 0:
        return x
    else:
        Q = x//y
        R = x%y
        gcd2(y,R)
        
gcd2(2,4)  










## Problem 2
## Write a function using recursion that returns prime numbers less than 121
#def find_primes(me = 121, primes = []):

def find_primes(number):
    primes = []
    for i in range(number):
        if i%2 !=0:
            primes.append(i)
            print (primes)
    

    

find_primes(121) 
 
## Problem 3
## Write a function that gives a solution to Tower of Hanoi game
## https://www.mathsisfun.com/games/towerofhanoi.html