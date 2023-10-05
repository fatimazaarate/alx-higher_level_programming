#!/usr/bin/python3
if __name__ == "__main__":
    import sys

arg_number = len(sys.argv) - 1
i = 1

if arg_number == 0:
    print("{} arguments." .format(arg_number))
elif arg_number == 1:
    print("{} argument." .format(arg_number))
    print("{}: {}" .format(arg_number, sys.argv[1]))
else:
        print("{} arguments:" .format(arg_number))
        while i <= arg_number:
            print("{}: {}" .format(i, sys.argv[i]))
            i = i+1
