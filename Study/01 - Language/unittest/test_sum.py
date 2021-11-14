import unittest
from calc import sum

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(sum(1,1), 2)
    def test(self):
        self.assertEqual(sum(2,2), 4)        
    
    
    
    