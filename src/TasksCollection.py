"""
Represents all tasks in the collection

Ravi Sinha
Apr 2013

"""

class TasksCollection(object):
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def __str__(self):
        for task in self.tasks:
            return task.task_info

