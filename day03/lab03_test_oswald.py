import unittest
from lab03_oswald import *

class labTests(unittest.TestCase):
	
	## fill in a few tests for each
	## make sure to account for correct and incorrect input

    def test_shout(self):
        with self.assertRaises(TypeError): shout(5) #Note: So we use with
        # with the self.assertRaises(TypeError): shout(5) to set it in 
        #the context of the function. It's what is usually done with 
        #assertRaises. 
        #Note: Check if it has to be used with the others. And also take
        #time to go through the other tests that can be done (i.e. those
        #that come after the dot)
            

    #def test_reverse(self):

    #def test_reversewords(self): 

    #def test_reversewordletters(self):

    #def test_piglatin(self):


if __name__ == '__main__':
  unittest.main()

