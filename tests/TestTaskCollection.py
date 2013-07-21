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
        global tasks
        global task_details_obtained
        user = 'Ravi Sinha'
        task = 'Do Laundry,2013,4,25'
        name = 'TestTask'
        tasks = TasksCollection(name)
        task_details_obtained = Task(task)

    def test_constuctor(self):
        self.assertEqual(tasks.name, 'TestTask')

    def test_adding_task(self):
        tasks.add(task_details_obtained)
        self.assertEqual(tasks.tasks[0].task_info, 'Do Laundry')

    def test_overdue_task(self):
        overdue_tasks = tasks.scan()
        self.assertEqual(overdue_tasks[0].task_info, 'Do Laundry')

if __name__ == '__main__':
    unittest.main()
