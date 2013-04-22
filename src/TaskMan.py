"""
Defines the class that contains one task's info
Reads a record with comma separated fields
Agnostic to whether the record was a string or a csv
"""


class TaskMan(object):
    def __init__(self, string):
        """ For simplicity, just year, month and date """
        items = string.strip().split(',')
        self.user = items[0]
        self.task_info = items[1]
        self.year = items[2]
        self.month = items[3]
        self.day = items[4]

