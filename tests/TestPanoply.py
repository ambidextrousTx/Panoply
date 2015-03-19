import unittest
import sys
sys.path.append('../src/')
from panoply_base import Panoply
import panoply


class PanoplyTest(unittest.TestCase):
    ''' Tests for the main Panoply class
    '''
    def setUp(self):
        ''' Nothing for now
        '''
        pass

    def test_sanity_false(self):
        ''' Not everything is allowed to go through the
        Panoply interface '''
        self.assertFalse(panoply.sanity_check('random string'))

    def test_sanity_true(self):
        ''' There is a set of expected commands for the
        Panoply interface '''
        self.assertTrue(panoply.sanity_check('display'))

    def test_get_command(self):
        ''' Currently the first word of a command line command
        is the one that gets passed on '''
        self.assertEqual(panoply.get_command('this is random'), 'this')

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
