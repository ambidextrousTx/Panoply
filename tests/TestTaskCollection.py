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
    def test_adding_task(self):
        tasks_collection = TasksCollection()
        task = Task('Ravi Sinha,Do Laundry,2013,4,25')
        tasks_collection.add(task)
        self.assertEqual(str(tasks_collection), task.task_info)
    
if __name__ == '__main__':
    unittest.main()
