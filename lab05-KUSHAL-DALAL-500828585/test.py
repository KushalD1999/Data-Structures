import unittest
from hashing import *


class test_Hashtable(unittest.TestCase):   

    def test_Get_GeneralCase(self):
        # Check the case where the element is present in the table; returns value        
        H = HashTable()
        H[54]="Data Structures"        
        self.assertEqual(H.get(54), 'Data Structures')
    
    def test_Get_InvalidCase(self):
        # Check the case where the element is not present in the table; returns None
        H = HashTable()
        H[10]="CPS305"        
        self.assertEqual(H.get(100), None)
    
    def test_put_GenralCase(self):
        # Check if the item is added in the table
        H=HashTable()
        H[54]="1"
        H[26]="2"
        self.assertEqual(H.get(54), '1')    
    
    def test_table_Resize(self):
        # Check the re-size of the table; returns new table size        
        H=HashTable()
        H[54]="1"
        H[26]="2"
        H[93]="3"
        H[17]="4"
        H[77]="5"
        H[31]="6"
        H[44]="7"
        H[55]="8"
        H[20]="9"
        # Putting an extra element would resize the table and the size would be 13(next prime number after default size 11)
        H[95]="10"
        H[96]="11"
        self.assertEqual(H.size, 13)
        
    
    def test_oldValue_after_Resize(self):
        # After the re-size of the table; you can still get the old values with the same keys        
        H=HashTable()
        H[54]="1"
        H[26]="2"
        H[93]="3"
        H[17]="4"
        H[77]="5"
        H[31]="6"
        H[44]="7"
        H[55]="8"
        H[20]="9"
        # Resizes Table here from size of 11 to 13
        H[95]="10"
        H[96]="11"
        self.assertEqual(H.get(54), '1')    

if (__name__ == "__main__"):            
    unittest.main(argv=['first-arg-is-ignored'],exit=False)



