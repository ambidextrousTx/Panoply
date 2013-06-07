"""
The main module for Panoply

Puts the user in a kind of a REPL
Allows the user to create TasksCollection's and Task's
The shell also corresponds to a Panoply object that handles requests

Ambidextrous
May 3, 2013
"""

from __future__ import print_function
from TasksCollection import TasksCollection
import sys

PANOPLY_VERSION = '0.1'


class Panoply(object):
    def __init__(self):
        self.task_collection_name = ''
        self.task_collection = ''
        self.user = ''
        self.status = ''

    def start(self, user, name):
        self.status = 'START'
        self.user = user
        self.task_collection_name = name
        self.task_collection = TasksCollection(user)

    def load(self, name):
        """ Load contents of a previously saved file """
        self.status = 'LOAD'
        pass

    def checkoff(self, task):
        """ Check off a task from the collection as done """
        self.status = 'CHECKOFF'
        pass

    def add(self, task):
        """ Add one task to the collection """
        self.status = 'ADD'
        if self.task_collection_name == '':
            print('Error: you need to create the task collection first.', end='\n')
            return
        else:
            self.task_collection.add(task)

    def scan(self):
        """ Scan the collection for any overdue tasks """
        self.status = 'SCAN'
        overdue_tasks = self.task_collection.scan()
        if len(overdue_tasks) == 0:
            print('Congratulations, no tasks overdue!', end="\n")
        else:
            print('Seems like you need to hustle!', end='\n')


def print_greeting():
    print('Welcome to Panoply version {0}'.format(PANOPLY_VERSION), end='\n')
    print('Created by Ravi Sinha during the summer of 2013', end='\n')
    print('You can create tasks, task collections and see which ones are overdue.', end='\n')
    print('You can also check some tasks off as being finished.', end='\n')
    print('Supported commands: start, load, add, scan, checkoff', end='\n')
    print('Press <Enter> by itself to exit.', end='\n')


def sanity_check(request):
    """ For now, see if the first word corresponds to one of the supported
    operations """
    return request.split(' ')[0] in ['add', 'scan', 'start', 'load', 'checkoff', '']


def get_command(request):
    return request.split(' ')[0]


def process_request(request):
    if not sanity_check(request):
        print('I cannot handle that.', end='\n')
        sys.exit(1)
    else:
        command = get_command(request)
        print('Command received: {0}'.format(command), end='\n')
        panoply = Panoply()
        # Calling the proper method using the string
        # Could not figure out how to use getattr because the methods
        # have different argument lists
        result = ''
        if command == 'start':
            print('Enter the user name: ', end='\n')
            user = raw_input()
            print('Enter the task name: ', end='\n')
            task = raw_input()
            result = panoply.start(user, name)
        print(result, end='\n')


def run_repl():
    request = 'X'
    while request != '':
        print('Panoply> ', end='')
        request = raw_input()
        process_request(request)
    print('Bye.', end='\n')


def main():
    print_greeting()
    run_repl()

if __name__ == '__main__':
    main()
