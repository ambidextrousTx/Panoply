import unittest
import sys
sys.path.append('../src/')
from panoply import Panoply


class PanoplyTest(unittest.TestCase):
    def test_start(self):
        p = Panoply()
        self.assertEqual(p.start('guest', 'sample'), 'I am the start method')

if __name__ == '__main__':
    unittest.main()
