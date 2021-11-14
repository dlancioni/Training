import unittest
from calc import sum, sub

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(sum(1,1), 0)
    def test(self):
        self.assertEqual(sub(2,1), 1)
    def test(self):
        self.assertEqual(sub(2,1), 99)    
    
    
    