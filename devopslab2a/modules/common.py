  
import datetime
import sys


def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform

def print_numbers(value):
    if value:
        for val in range(0,101,2):
            print(val)
    else:
        for val in range(1,100,2):
            print(val)

def wrong_function():
    a = 0
    b = 1
    print(b/a)