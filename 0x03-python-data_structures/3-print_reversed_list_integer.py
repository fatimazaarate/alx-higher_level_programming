#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return None
    rev_list = list(reversed(my_list))
    for item in rev_list:
        print("{:d}" .format(item))
