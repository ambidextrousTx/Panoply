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

    def test_str_repr(self):
        """ Test the string representation of the task """
        task = 'Ravi Sinha,Do Laundry,2013,4,25'
        task_details_obtained = TaskMan(task)
        self.assertEqual(str(task_details_obtained), 'Ravi Sinha, task Do Laundry, due 4-25-2013')

    def test_repr_repr(self):
        """ Test the string representation of the task """
        task = 'Ravi Sinha,Do Laundry,2013,4,25'
        task_details_obtained = TaskMan(task)
        self.assertEqual(repr(task_details_obtained), 'Ravi Sinha, task Do Laundry, due 4-25-2013')

    def test_overdue(self):
        """ Test the overdue test """
        task = 'Ravi Sinha,Do Laundry,2013,4,19'
        task_details_obtained = TaskMan(task)
        self.assertTrue(task_details_obtained.is_overdue()) 

    def test_overdue_negative(self):
        """ Test when not overdue """
        task = 'Ravi Sinha,Fly to Moon,9999,4,25'
        task_details_obtained = TaskMan(task)
        self.assertFalse(task_details_obtained.is_overdue())

if __name__ == '__main__':
    unittest.main()
