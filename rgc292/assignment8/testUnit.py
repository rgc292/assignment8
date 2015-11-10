'''
Created on Nov 10, 2015

@author: Rafael Garcia (rgc292)
'''
import unittest
import business as bs
"""This class is intended to check if the validation input is working and if the 
   creation of a distribution is working"""

class Test(unittest.TestCase):
    
    #Test the validate_input method
    def test_validate_input(self):
        self.business = bs.Calculation()
        self.result = self.business.validate_input()
        self.assert_(self.result in range(0, 2000))
            
    
    #Test the distribution_wins_loses method
    def test_distribution(self):
        self.business = bs.Calculation()
        self.result = self.business.distribution_wins_loses(5)
        self.assert_(self.result[0] == -1 or self.result[0] == 1)      
        
   
        