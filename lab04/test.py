import unittest
from mySolution import *

class test_power(unittest.TestCase):

    def test_power_GeneralCase(self):
        self.assertEqual(power(2,3, 1), 8)
        
    def test_power_BaseCase(self):
        self.assertEqual(power(2,0, 1), 1)
    
    def test_power_GreaterNumberCase(self):
        self.assertEqual(power(2,100, 1), 1267650600228229401496703205376)
    
    def test_power_NegativeCase(self):
        self.assertEqual(power(-2,5, 1), -32)

class test_powerH(unittest.TestCase):
    
    def test_powerH_GeneralCase(self):
        self.assertEqual(powerH(2,3), 8)
    
    def test_powerH_BaseCase(self):
        self.assertEqual(powerH(9,0), 1)
    
    def test_powerH_GreaterNumberCase(self):
        self.assertEqual(powerH(3,100), 515377520732011331036461129765621272702107522001)
    
    def test_powerH_NegativeCase(self):
        self.assertEqual(powerH(-3,3), -27)

class test_C(unittest.TestCase):
    
    def test_C_BaseCase(self):
        self.assertEqual(C(0,0), 1)     
    
    def test_C_GeneralCase(self):
        self.assertEqual(C(10,4), 210)      

if (__name__ == "__main__"):            
    unittest.main(argv=['first-arg-is-ignored'],exit=False)