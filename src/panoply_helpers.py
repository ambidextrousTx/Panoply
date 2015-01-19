'''
Helper methods used in the operation of Panoply

Ambidextrous, Jan 2015
'''

from datetime import date


def compute_late_days(task):
    ''' Count the number of days between the current date
    and the original date set for the task, and return the
    delta in the number of days (string)
    '''
    currdate = date.today()
    # Months are counted from 1 in most libraries
    origdate = date(int(task.year), int(task.month) + 1, int(task.day))
    delta = currdate - origdate
    return str(delta.days)
