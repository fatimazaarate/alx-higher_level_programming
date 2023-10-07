#!/usr/bin/env python3
def no_c(my_string):
    new_string = [char for char in my_string if char != 'c' and char != 'C']
    result = ''
    for s in new_string:
        result += s
    return result
