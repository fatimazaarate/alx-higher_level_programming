#!/usr/bin/python3
if __name__ == "__main__":
    import sys

arg_number = len(sys.argv) - 1

if arg_number == 0:
    print("{} arguments." .format(arg_number))
elif arg_number == 1:
    print("{} argument." .format(arg_number))
else:
    print("{} arguments:" .format(arg_number))
for i in range(arg_number):
    print("{}: {}" .format(i+1, sys.argv[i+1]))

