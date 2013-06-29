"""
The main module for Panoply

Puts the user in a kind of a REPL
Allows the user to create TasksCollection's and Task's
The shell also corresponds to a Panoply object that handles requests

Ambidextrous
May 3, 2013
"""

from __future__ import print_function
import sys
import csv
from Task import Task
from panlib import InvalidStateException
from TasksCollection import TasksCollection

PANOPLY_VERSION = '0.1'


class Panoply(object):
    def __init__(self):
        self.task_collection_name = ''
        self.task_collection = ''
        self.user = ''
        self.status = ''

    def start(self):
        self.status = 'START'
        print('Enter the user name: ', end='\n')
        user = raw_input()
        print('Enter the task collection name: ', end='\n')
        task = raw_input()
        self.user = user
        self.task_collection_name = task
        self.task_collection = TasksCollection(user)

    def load(self):
        """ Load contents of a previously saved file """
        """ Currently supporting only one file """
        self.status = 'LOAD'
        with open('panoply_tasks.pan', 'r') as csvfile:
            taskreader = csv.reader(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for row in taskreader:
                print(', '.join(row), end='\n')
        print('Done loading from file panoply_tasks.pan', end='\n')

    def checkoff(self, task):
        """ Check off a task from the collection as done """
        self.status = 'CHECKOFF'
        pass

    def add(self):
        """ Add one task to the collection.
        Can only add if the status is START
        """
        if self.status != 'START':
            raise InvalidStateException
        else:
            self.status = 'ADD'
            print('Enter the task info: ', end='\n')
            task_info = raw_input()
            print('Enter the date (yyyy,mm,dd): ', end='\n')
            date = raw_input()
            self.task_collection.add(Task('{0},{1}'.format(task_info, date)))

    def scan(self):
        """ Scan the collection for any overdue tasks """
        self.status = 'SCAN'
        overdue_tasks = self.task_collection.scan()
        if len(overdue_tasks) == 0:
            print('Congratulations, no tasks overdue!', end="\n")
        else:
            print('Seems like you need to hustle!', end='\n')

    def save(self):
        """ Save the current task collection on disk """
        with open('panoply_tasks.pan', 'a') as csvfile:
            taskwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for task in self.task_collection.tasks:
                taskwriter.writerow([self.user, self.task_collection_name, task.task_info, task.year, task.month, task.day])
        print('Done saving to file panoply_tasks.pan', end='\n')


def print_greeting():
    print('Welcome to Panoply version {0}'.format(PANOPLY_VERSION), end='\n')
    print('Created by Ravi Sinha during the summer of 2013', end='\n')
    print('You can create tasks or task collections, and see which ones '
          'are overdue.', end='\n')
    print('It is possible to save a collection and also load it later',
          end='\n')
    print('You can also check some tasks off as being finished.', end='\n')
    print('Supported commands: start, load, add, scan, checkoff, save',
          end='\n')
    print('Press <Enter> by itself to exit.', end='\n')


def sanity_check(request):
    """ For now, see if the first word corresponds to one of the supported
    operations """
    return request.split(' ')[0] in ['add', 'scan', 'start', 'load',
                                     'checkoff', 'save', '']


def get_command(request):
    return request.split(' ')[0]


def checkoff(panoply):
    # Can only add if the status is LOAD or ADD
    if panoply.status not in ['LOAD', 'ADD']:
        raise InvalidStateException
    else:
        pass


def process_request(request, panoply):
    if not sanity_check(request):
        print('I cannot handle that.', end='\n')
        sys.exit(1)
    else:
        command = get_command(request)
        print('Command received: {0}'.format(command), end='\n')
        # Calling the proper method using the string
        # Could not figure out how to use getattr because the methods
        # have different argument lists
        result = ''
        if command == 'start':
            panoply.start()
        elif command == 'add':
            panoply.add()
        elif command == 'checkoff':
            panoply.checkoff()
        elif command == 'scan':
            panoply.scan()
        elif command == 'load':
            panoply.load()
        elif command == 'save':
            panoply.save()

        print(result, end='\n')


def run_repl():
    request = 'X'
    panoply = Panoply()
    while request != '':
        print('Panoply> ', end='')
        request = raw_input()

        # Needs must keep the same object for state to work
        process_request(request, panoply)
    print('Bye.', end='\n')


def main():
    print_greeting()
    run_repl()

if __name__ == '__main__':
    main()
