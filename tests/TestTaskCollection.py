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
    def test_constuctor(self):
        user = 'Ravi Sinha'
        tasks = TasksCollection(user)
        self.assertEqual(tasks.user, 'Ravi Sinha')
        
    
if __name__ == '__main__':
    unittest.main()
