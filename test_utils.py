# test_utils.py
# Author: Sébastien Combéfis
# Version: February 2, 2016

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(utils.fact(5),120)
        self.assertEqual(utils.fact(3),6)
        pass
    
    def test_roots(self):
        self.assertNotEquals(utils.roots(4,4,1),-0.5)
        pass
    def test_integrate(self):
        self.assertEquals(utils.integrate('x ** 2 - 1', -1,1),-1.3333)
        pass
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful()) 
