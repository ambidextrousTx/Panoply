"""
Defines the class that contains one task's info
Reads a record with comma separated fields
Agnostic to whether the record was a string or a csv

Ravi Sinha
Apr 2013
"""

from datetime import datetime


class Task(object):
    def __init__(self, string):
        """ For simplicity, just year, month and date """
        items = string.strip().split(',')
        self.task_info = items[2]
        self.year = items[3]
        self.month = items[4]
        self.day = items[5]
        self.status = items[6]

    def __str__(self):
        return 'Task {0}, due {1}-{2}-{3}'.format(self.task_info, self.month, self.day, self.year) 

    def __repr__(self):
        return 'Task {0}, due {1}-{2}-{3}'.format(self.task_info, self.month, self.day, self.year) 

    def is_overdue(self):
        """ Return if the task in question is overdue """
        date = datetime.now()
        due_date = datetime(int(self.year), int(self.month), int(self.day), 23, 59, 59)
        return date > due_date
