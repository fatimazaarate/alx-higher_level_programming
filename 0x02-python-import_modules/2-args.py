#!/usr/bin/python3
import sys

arg_number = len(sys.argv) - 1

for args in sys.argv:
    if arg_number == 0:
        print("{} arguments." .format(arg_number))
    elif arg_number == 1:
        print("{} argument:" .format(arg_number))
        print("{}: {}" .format(arg_number, args))
    '''else:
        print("{} arguments:" .format(arg_number))
        print("{}: {}" .format(arg_number, sys.argv[1:]))'''

