'''
The Panoply class
Manages everything about a task collection
'''

from __future__ import print_function
import csv
from Task import Task
from commands import getstatusoutput
from TasksCollection import TasksCollection
import panoply_helpers


class Panoply(object):
    def __init__(self):
        self.task_collection_name = ''
        self.task_collection = ''
        self.user = ''

    def start(self):
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
        # Reload everything from the file into the object
        # self.task_collection_name = 'NewCollection'
        # self.user = 'NewUser'
        # self.task_collection = TasksCollection(self.task_collection_name, self.user)
        loaded_tasks_details_list = []
        with open('panoply_tasks.pan', 'r') as csvfile:
            taskreader = csv.reader(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            # Loading tasks from file into object and printing
            for row in taskreader:
                joined_row = ','.join(row)
                print(joined_row, end='\n')
                loaded_tasks_details_list.append(joined_row)

                # self.task_collection.add(Task(','.join(row)))

        self.user = loaded_tasks_details_list[0].split(',')[0]
        self.task_collection_name = loaded_tasks_details_list[0].split(',')[1]
        self.task_collection = TasksCollection(self.task_collection_name, self.user)

        for row in loaded_tasks_details_list:
            self.task_collection.add(Task(row))

        print('\nDone loading from file panoply_tasks.pan', end='\n')

    def checkoff(self):
        """ Check off a task from the collection as done """
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
        """
        # Check if a task collection has been loaded
        print(self.user, end='\n') 
        print(self.task_collection_name, end='\n')
        print('Enter the task details: ', end='\n')
        task_info = raw_input()
        print('Enter the date (yyyy,mm,dd): ', end='\n')
        date = raw_input()
        self.task_collection.add(Task(',,{0},{1}'.format(task_info, date)))
        self.save()

    def delete(self):
        """ Delete a given task from the collection.
        """
        print('Enter the description of the task to be deleted: ', end='\n')
        task_info = raw_input()
        for task in self.task_collection.tasks:
            if task.task_info == task_info:
                self.task_collection.tasks.remove(task)
                print('Task successfully deleted', end='\n')
                self.save()
                return
        print('Task not found in collection', end='\n')

    def scan(self):
        """ Scan the collection for any overdue tasks """
        overdue_tasks = self.task_collection.scan()
        if len(overdue_tasks) == 0:
            print('\nCongratulations, no tasks overdue!', end="\n")
        else:
            print('\nSeems like you need to hustle!', end='\n')
            print('Here are your overdue tasks', end='\n')
            for task in overdue_tasks:
            	late_by_days = panoply_helpers.compute_late_days(task)
                print('{0}, overdue {1} days'.format(task.task_info, late_by_days), end='\n')

    def display(self):
        ''' Just displays the contents of the currently loaded or used
        collection '''
        self.load()
        if len(self.task_collection.tasks) == 0:
            print('\nNothing to display yet.', end='\n')
        else:
            for task in self.task_collection.tasks:
                print('', end='\n')
                print(self.task_collection.user, end=',')
                print(self.task_collection_name, end=',')
                print(task.task_info, end=',')
                print(task.year, end=',')
                print(task.month, end=',')
                print(task.day, end=',')
                print(task.status, end='\n')

    def save(self):
        """ Save the current task collection on disk """
        with open('panoply_tasks.pan', 'w') as csvfile:
            taskwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for task in self.task_collection.tasks:
                taskwriter.writerow([self.user, self.task_collection_name, task.task_info, task.year, task.month, task.day])
        print('\nDone saving to file panoply_tasks.pan', end='\n')
