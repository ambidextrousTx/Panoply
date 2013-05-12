"""
The main module for Panoply

Puts the user in a kind of a REPL
Allows the user to create TasksCollection's and Task's
The shell also corresponds to a Panoply object that handles requests

No unit tests for this module, yet

Ambidextrous
May 3, 2013
"""

from __future__ import print_function
import sys

PANOPLY_VERSION = '0.1'

def Panoply(object):
    def __init__(self):
        self.task_collection_name = ''

    def start(self, name):
        self.task_collection_name = name

    def load(self, name):
        """ Load contents of a previously saved file """
        pass

    def add(self, task):
        """ Add one task to the collection """
        pass

    def scan(self):
        """ Scan the collection for any overdue tasks """
        pass

def print_greeting():
    print('Welcome to Panoply version {0}'.format(PANOPLY_VERSION), end = '\n')
    print('Created by Ravi Sinha during the summer of 2013', end = '\n')
    print('You can create tasks, task collections and see which ones are overdue.', end = '\n')
    print('Supported commands: start, load, add, scan', end = '\n')
    print('Press <Enter> by itself to exit.', end = '\n')

def sanity_check(request):  
    """ For now, see if the first word corresponds to one of the supported
    operations """
    return request.split(' ')[0] in ['add', 'scan', 'start', 'load']

def get_command(request):
    return request.split(' ')[0]

def process_request(request):
    if not sanity_check(request):
        print('I cannot handle that.', end = '\n')
        sys.exit(1)
    else:
        command = get_command(request)
        
def run_repl():
    request = 'X'
    while request != '':
        print('Panoply> ', end = '')
        request = raw_input()
        process_request(request)
    print('Bye.', end = '\n')

def main():
    print_greeting()
    run_repl()

if __name__ == '__main__':
    main()
