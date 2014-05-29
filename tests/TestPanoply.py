import unittest
import sys
sys.path.append('../src/')
from panoply_base import Panoply
import panoply


class PanoplyTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_sanity(self):
        self.assertFalse(panoply.sanity_check('random string'))

    def test_get_command(self):
        self.assertEqual(panoply.get_command('this is random'), 'this')

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
