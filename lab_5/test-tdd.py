from biqr_lab1 import sys, math, get_coef, get_roots
import unittest

class BiQrTest(unittest.TestCase):

    def test_1(self):
        self.assertEqual(get_roots(1,5,-36),[2,-2])


    def test_2(self):
        self.assertEqual(get_roots(3,5,6),[])


    def test_3(self):

        with self.assertRaises(ValueError):
            get_coef('input')
            
if __name__ == '__main__':
    unittest.main()
         
