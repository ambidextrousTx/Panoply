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

def run_repl():
    request = 'X'
    while request != '':
        print('Panoply> ', end = '')
        request = raw_input()
    print('Bye.', end = '\n')

def main():
    print_greeting()
    run_repl()

if __name__ == '__main__':
    main()
