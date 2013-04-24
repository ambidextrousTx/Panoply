"""
Defines the class that contains one task's info
Reads a record with comma separated fields
Agnostic to whether the record was a string or a csv
"""

from datetime import datetime

class TaskMan(object):
    def __init__(self, string):
        """ For simplicity, just year, month and date """
        items = string.strip().split(',')
        self.user = items[0]
        self.task_info = items[1]
        self.year = items[2]
        self.month = items[3]
        self.day = items[4]

    def __str__(self):
        return '{0}, task {1}, due {2}-{3}-{4}'.format(self.user, self.task_info, self.month, self.day, self.year) 
        
    def __repr__(self):
        return '{0}, task {1}, due {2}-{3}-{4}'.format(self.user, self.task_info, self.month, self.day, self.year) 

    def is_overdue(self):
        """ Return if the task in question is overdue """
        date = datetime.now()
        due_date = datetime(int(self.year), int(self.month), int(self.day), 23, 59, 59)
        return date > due_date
        
