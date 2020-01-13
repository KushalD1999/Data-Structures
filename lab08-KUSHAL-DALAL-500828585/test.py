import unittest
from parsers import *

class test_evalTree(unittest.TestCase):

    def test_evalTree_Basic(self):
        self.assertEqual(parse(["3"]), ['3', [], []])
        
    def test_evalTree_Base(self):
        self.assertEqual(parse(['8', '+', '8']), ['+', ['8', [], []], ['8', [], []]])
    
    def test_generate_twoOperatorsDifferentPrecedence(self):
        self.assertEqual(parse(['3', '+', '5', '*', '1']), ['+', ['3', [], []], ['*', ['5', [], []], ['1', [], []]]])  
    
    def test_generate_twoOperatorsSamePrecedence(self):
        self.assertEqual(parse(['3', '+', '5', '+', '1']), ['+', ['+', ['3', [], []], ['5', [], []]], ['1', [], []]])  
    
    def test_generate_threeOperators(self):
        self.assertEqual(parse(['3', '+', '5', '*', '1' , '-' , '6']), ['-', ['+', ['3', [], []], ['*', ['5', [], []], ['1', [], []]]], ['6', [], []]])  
        
    def test_evalTree_BracketCase(self):
        self.assertEqual(parse([['4', '+', '3'], '*', '7']),['*', ['+', ['4', [], []], ['3', [], []]], ['7', [], []]])
        
    def test_evalTree_singleFactorialCase(self):
        self.assertEqual(parse(['8', '!']),['!', ['8', [], []], []] )
        
    def test_evalTree_BracketFactorialCase(self):
        self.assertEqual(parse(['10','/',['3', '!'],'-', '1']), ['-', ['/', ['10', [], []], ['!', ['3', [], []], []]], ['1', [], []]])
        
    def test_evalTree_ComplexCase(self):
        self.assertEqual(parse(['2', '+', ['9', '!']]), ['+', ['2', [], []], ['!', ['9', [], []], []]])        

if (__name__ == "__main__"):            
    unittest.main(argv=['first-arg-is-ignored'],exit=False)