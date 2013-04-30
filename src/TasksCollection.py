"""
Represents all tasks in the collection

Ravi Sinha
Apr 2013

"""

class TasksCollection(object):
    def __init__(self, user):
        self.user = user
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)


