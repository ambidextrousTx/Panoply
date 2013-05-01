"""
Testing TasksCollection

Ravi Sinha
Apr 2013
"""

import sys
import unittest
sys.path.append('../src/')
from TasksCollection import TasksCollection
from Task import Task

class TestTaskCollection(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        user = 'Ravi Sinha'
        global tasks
        tasks = TasksCollection(user)

    def test_constuctor(self):
        self.assertEqual(tasks.user, 'Ravi Sinha')

    
if __name__ == '__main__':
    unittest.main()
