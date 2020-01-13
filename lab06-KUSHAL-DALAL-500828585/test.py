import unittest, random
from sorting import *

class m03_Sorting_Testing(unittest.TestCase):
    
    def test_m03Sort_EmptySetCase(self):
        self.assertEqual(m03_quickSort([]), None)    
    
    def test_m03Sort_GenralCase(self):
        alist = random.sample(range(1, 20), 15)
        retOutput = alist.sort()
        self.assertEqual(m03_quickSort(alist), retOutput)
        
    def test_m03Sort_MediumDataSetCase(self):
        alist = random.sample(range(1, 100), 50)
        retOutput = alist.sort()
        self.assertEqual(m03_quickSort(alist), retOutput)    
        
    def test_m03Sort_largeDatasetCase(self):
        alist = random.sample(range(1, 2000), 1000)
        retOutput = alist.sort()
        self.assertEqual(m03_quickSort(alist), retOutput)    
    
    
if (__name__ == "__main__"):            
    unittest.main(argv=['first-arg-is-ignored'],exit=False)