"""
The main module for Panoply

Puts the user in a kind of a REPL
Allows the user to create TasksCollection's and Task's
The shell also corresponds to a Panoply object that handles requests

Ambidextrous
Summer, 2013
"""

from __future__ import print_function
from panoply_base import Panoply
import sys

PANOPLY_VERSION = '0.1'


def print_greeting():
    ''' Print beginning greeting and version information
    '''
    print('Welcome to Panoply version {0}'.format(PANOPLY_VERSION), end='\n')
    print('Created by Ravi Sinha', end='\n')
    print('You can create tasks or task collections, and see which ones '
          'are overdue.', end='\n')
    print('You can check tasks off as finished.', end='\n')
    print('You can save collections and load them later.', end='\n')


def print_help():
    ''' Prints help. Can be called anytime
    '''
    print('Supported commands: start, load, display, add, delete, scan, checkoff, save, help', end='\n')
    print('Press <Enter> by itself or enter quit, exit, etc. to exit.', end='\n')


def sanity_check(request):
    ''' For now, see if the first word corresponds to one of the supported
    operations '''
    return request.split(' ')[0] in ['add', 'scan', 'start', 'load', 'checkoff', 'save', '', 'bye', 'quit', 'exit', 'q', 'help', 'delete', 'display']


def get_command(request):
    ''' Logical encapsulation: returns the command requested
    '''
    return request.split(' ')[0]


def process_request(request, panoply):
    ''' Switches over the command requested and performs
    relevant operation
    '''
    if not sanity_check(request):
        print('I cannot handle that. Please refer to the help.', end='\n')
        print_help()
    else:
        command = get_command(request)
        print('Command received: {0}'.format(command), end='\n')
        # Calling the proper method using the string
        # Could not figure out how to use getattr because the methods
        # have different argument lists
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
        elif command == 'delete':
            panoply.delete()
        elif command == 'display':
            panoply.display()
        elif command == 'help':
            print_help()


def run_repl():
    ''' Continuously run the Panoply REPL until
    called off '''
    request = 'X'
    panoply = Panoply()
    while request not in ['', 'exit', 'quit', 'q', 'bye']:
        print('Panoply> ', end='')
        request = raw_input()

        # Needs must keep the same object for state to work
        process_request(request, panoply)
    print('Bye.', end='\n')


def main():
    ''' Here's where everything starts
    '''
    print_greeting()
    print_help()
    run_repl()

if __name__ == '__main__':
    main()
