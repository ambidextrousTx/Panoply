"""
The main module for Panoply

Puts the user in a kind of a REPL
Allows the user to create TasksCollection's and Task's

No unit tests for this module

Ambidextrous
May 3, 2013
"""

from __future__ import print_function
import sys

PANOPLY_VERSION = '0.1'

def print_greeting():
    print('Welcome to Panoply version {0}'.format(PANOPLY_VERSION), end = '\n')
    print('Created by Ravi Sinha during the summer of 2013', end = '\n')
    print('You can create tasks, task collections and see which ones are overdue.', end = '\n')
    print('Press <Enter> by itself to exit.', end = '\n')

def sanity_check(request):  
    """ For now, see if the first word corresponds to one of the supported
    operations """
    return request.split(' ')[0] in ['add', 'scan', 'is_overdue']

def process_request(request):
    if sanity_check(request):
        print('I can handle that.', end = '\n')

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
