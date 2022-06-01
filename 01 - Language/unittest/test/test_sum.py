import sys
sys.path.append("..")

import unittest
from src.calc import Calc

class TestSum(unittest.TestCase):

    #run before execute tests    
    def setUp(self):
        self.calc = Calc()

    def test_sum(self):
        self.assertEqual(self.calc.sum(1,1), 2)

    #run after execute tests
    def tearDown(self):
        self.calc = ""

if __name__ == '__main__':
    unittest.main()        