import unittest
from eval import *

class test_evalTree(unittest.TestCase):

    def test_evalTree_EmptyTreeCase(self):
        self.assertEqual(evalTree([[], [], []], [["a", 10], ["b", 20]]), None)
    
    def test_evalTree_OnlyRoot(self):
        self.assertEqual(evalTree(["100", [], []], [["a", 10], ["b", 20]]), 100)
        
    def test_evalTree_ZeroDivisionCase(self):
        self.assertEqual(evalTree(["/", ["X", [], []], ["Y", [], []]], [["X", 80], ["Y",0]]), None)
    
    def test_evalTree_InvalidTree(self):
        self.assertEqual(evalTree(["+", ["a", [], []], ["*", ["b", [], []],["c", [], []]]], [["b", 20], ["c", 30]]), None)        
    
    def test_evalTree_LongTree(self):
        self.assertEqual(evalTree(["*", ["+", ["A", [], []], ["B", [], []]], ["+", ["C", [], []],["D", [], []]]], [["D", 5], ["C", 50], ["B", 500], ["A", 5000]]), 302500)        
        
    def test_evalTree_MultiplyEachChildCase(self):
        self.assertEqual(evalTree(["*", ["K", [], []], ["D", [], []]], [["K", 80], ["D", 40], ["c",30]]), 3200)          

    def test_evalTree_AdditionEachChildCase(self):
        self.assertEqual(evalTree(["+", ["K", [], []], ["D", [], []]], [["K", 80], ["D", 90]]), 170)          

    def test_evalTree_SubstractEachChildCase(self):
        self.assertEqual(evalTree(["-", ["T", [], []], ["D", [], []]], [["D", 80], ["T", 40]]),-40)          

    def test_evalTree_DivideEachChildCase(self):
        self.assertEqual(evalTree(["/", ["K", [], []], ["D", [], []]], [["K", 80], ["D", 40], ["c",30]]), 2)          


if (__name__ == "__main__"):            
    unittest.main(argv=['first-arg-is-ignored'],exit=False)