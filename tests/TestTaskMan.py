import sys
import unittest
sys.path.append('../src/')
from TaskMan import TaskMan

class TestTaskMan(unittest.TestCase):
    def test_constructor_string(self):
        """ Test the constructor of TaskMan for string record """
        task = 'Ravi Sinha,Do Laundry,2013,4,25'
        task_details_obtained = TaskMan(task)
        self.assertEqual(task_details_obtained.user, 'Ravi Sinha')
        self.assertEqual(task_details_obtained.task_info, 'Do Laundry')
        self.assertEqual(task_details_obtained.year, '2013')
        self.assertEqual(task_details_obtained.month, '4')
        self.assertEqual(task_details_obtained.day, '25')

if __name__ == '__main__':
    unittest.main()

