import sys
sys.path.append("..")

import unittest
from src.calc import Calc

class TestSub(unittest.TestCase):

    #run before tests
    def setUp(self):
        self.calc = Calc()    

    def test_sub(self):
        c = Calc()
        self.assertEqual(c.sub(2,1), 1)

    #run after tests
    def tearDown(self):
        self.calc = ""        

if __name__ == '__main__':
    unittest.main()