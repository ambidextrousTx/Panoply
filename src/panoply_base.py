'''
The Panoply class
Manages everything about a task collection
'''

from __future__ import print_function
import csv
from Task import Task
from commands import getstatusoutput
from panlib import InvalidStateException
from TasksCollection import TasksCollection


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
        self.task_collection = TasksCollection(task, user)

        response = 'Created a new collection {0} for user {1}'.format(task, user)
        print(response)

    def load(self):
        """ Load contents of a previously saved file """
        """ Currently supporting only one file """
        self.status = 'LOAD'
        # Reload everything from the file into the object
        self.task_collection_name = 'NewCollection'
        self.user = 'NewUser'
        self.task_collection = TasksCollection(self.task_collection_name, self.user)
        with open('panoply_tasks.pan', 'r') as csvfile:
            taskreader = csv.reader(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            # Loading tasks from file into object and printing
            for row in taskreader:
                print(', '.join(row), end='\n')
                self.task_collection.add(Task(','.join(row)))

        print('\nDone loading from file panoply_tasks.pan', end='\n')

    def checkoff(self):
        """ Check off a task from the collection as done """
        # Can only add if the status is LOAD or ADD or CHECKOFF
        if self.status not in ['LOAD', 'ADD', 'CHECKOFF']:
            raise InvalidStateException
        else:
            self.status = 'CHECKOFF'
            print('What collection?', end='\n')
            coll = raw_input()
            print('Enter the task info to check off:', end='\n')
            task = raw_input()
            # Add logic to check if the task exists
            # Sequential search for now
            flag = False
            with open('panoply_tasks.pan', 'r') as csvfile:
                taskreader = csv.reader(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                for row in taskreader:
                    task_coll = row[1]
                    task_info = row[2]
                    if task_coll == coll and task_info == task:
                        print('\nFound the task!', end='\n')
                        print('Checking off the task ... done', end='\n')
                        flag = True
                        break
            if flag:
                # Add logic to delete task
                taskreader = csv.reader(open('panoply_tasks.pan', 'r'), delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                writer = csv.writer(open('corrected.csv', 'w'), delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                for row in taskreader:
                    if not (row[1] == task_coll and row[2] == task_info):
                        writer.writerow(row)
                # Move old file to new
                moved = getstatusoutput('mv corrected.csv panoply_tasks.pan')

            else:
                print('Task not found!')

    def add(self):
        """ Add one task to the collection.
        Can only add if the status is START, LOAD, CHECKOFF
        """
        if self.status not in ['START', 'LOAD', 'CHECKOFF']:
            raise InvalidStateException
        else:
            self.status = 'ADD'
            print('Enter the task details: ', end='\n')
            task_info = raw_input()
            print('Enter the date (yyyy,mm,dd): ', end='\n')
            date = raw_input()
            self.task_collection.add(Task(',,{0},{1}'.format(task_info, date)))
            self.save()

    def delete(self):
        """ Delete a given task from the collection.
        Can only delete if the status is ADD?
        """
        pass

    def scan(self):
        """ Scan the collection for any overdue tasks """
        self.status = 'SCAN'
        overdue_tasks = self.task_collection.scan()
        if len(overdue_tasks) == 0:
            print('\nCongratulations, no tasks overdue!', end="\n")
        else:
            print('\nSeems like you need to hustle!', end='\n')
            for task in overdue_tasks:
                print('{0}'.format(task.task_info), end='\n')

    def display(self):
        ''' Just displays the contents of the currently loaded or used
        collection '''
        if self.status not in ['LOAD', 'ADD', 'SCAN', 'CHECKOFF']:
            print('\nNothing to display yet.', end='\n')
        else:
            for task in self.task_collection.tasks:
                print('', end='\n')
                print(self.task_collection.user, end=',')
                print(self.task_collection_name, end=',')
                print(task.task_info, end=',')
                print(task.year, end=',')
                print(task.month, end=',')
                print(task.day, end='\n')

    def save(self):
        """ Save the current task collection on disk """
        with open('panoply_tasks.pan', 'w') as csvfile:
            taskwriter = csv.writer(csvfile, delimiter=',',
                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for task in self.task_collection.tasks:
                taskwriter.writerow([self.user, self.task_collection_name, task.task_info, task.year, task.month, task.day])
        print('\nDone saving to file panoply_tasks.pan', end='\n')
