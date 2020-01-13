import unittest
from mySolution import *

class test_genrate(unittest.TestCase):

    def test_given_BaseCase(self):
        self.assertEqual(infixToPostfixEval("( 2 + 2 ) ! + 8"), ('2 2 + ! 8 +', 32))
    
    def test_smaller_length_OperationCase(self):
        self.assertEqual(infixToPostfixEval("( 9 * 9 )"), ('9 9 *', 81))
    
    def test_longer_Length_OperationCase(self):
        self.assertEqual(infixToPostfixEval("( ( ( ( 8 * 2 + 3 / 2 - 9 ) * 2 / 1 + 9 * 3 ) + 3 ! ) + 9 ! + 8 ! ) + ( 2 * 3 / 2 )"), ('8 2 * 3 2 / + 9 - 2 * 1 / 9 3 * + 3 ! + 9 ! + 8 ! + 2 3 * 2 / +', 403253.0))
    
    def test_no_BracketCase(self):
        self.assertEqual(infixToPostfixEval("1 + 2 + 3 - 4 * 5 * 6 * 7 / 8 + 9 !"), ('1 2 + 3 + 4 5 * 6 * 7 * 8 / - 9 ! +', 362781.0))    
    
    def test_AdditionCase(self):
        self.assertEqual(infixToPostfixEval("( ( 8 + 2 ) + 9 ) + 4 + ( 6 + 2 ) + 5 + 3 + ( 3 + 1 )"), ('8 2 + 9 + 4 + 6 2 + + 5 + 3 + 3 1 + +', 43))
        
    def test_SubstractionCase(self):
        self.assertEqual(infixToPostfixEval("( ( 9 - 2 ) - 2 ! ) * ( 2 ! - 3 ! )"), ('9 2 - 2 ! - 2 ! 3 ! - *', -20))  
        
    def test_MultiplicationCase(self):
        self.assertEqual(infixToPostfixEval("( ( 5 * 2 ) * 2 ) * ( 6 * 3 )"), ('5 2 * 2 * 6 3 * *', 360))
        
    def test_DivisionCase(self):
        self.assertEqual(infixToPostfixEval("( 8 / 2 ) / 2 * ( 9 / 3 ) * ( 3 / 1 )"), ('8 2 / 2 / 9 3 / * 3 1 / *', 18.0))
        
    def test_FactorialCase(self):
        self.assertEqual(infixToPostfixEval("( ( 5 * 2 ) ! + 3 ! ) * ( 6 ! * 3 ! )"), ('5 2 * ! 3 ! + 6 ! 3 ! * *', 15676441920)) 
    
    def test_ZeroCase(self):
        self.assertEqual(infixToPostfixEval("( 0 + 0 ) + 0 + 0 + 0"), ('0 0 + 0 + 0 + 0 +', 0))    

if (__name__ == "__main__"):            
    unittest.main(argv=['first-arg-is-ignored'],exit=False)



