"""
Represents all tasks in the collection

Ravi Sinha
Apr 2013

"""


class TasksCollection(object):
    def __init__(self, name, user):
        self.name = name
        self.user = user
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def scan(self):
        """ Scan all tasks in tasks[] and report which ones
        are overdue
        """
        overdue_tasks = []
        for task in self.tasks:
            if task.is_overdue():
                overdue_tasks.append(task)

        return overdue_tasks
