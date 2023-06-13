import unittest

class OperatorsTest(unittest.TestCase):
    def test_equal_operator(self):
        a = 7
        b = 7
        self.assertTrue(a == b)

    def test_notequal_operator(self):    
        a = 3
        b = 8    
        self.assertTrue(a != b)
    
    def test_less_operator(self):    
        a = 3
        b = 9
        self.assertTrue(a < b)

    def test_greater_operator(self):    
        a = 9
        b = 3    
        self.assertTrue(a > b)

    def test_less_equal_operator(self):    
        a = 10
        b = 10
        self.assertTrue(a <= b)

    def test_greater_equal_operator(self):    
        a = 31
        b = 13    
        self.assertTrue(a >= b)

 
if __name__ == '__main__':
    unittest.main()