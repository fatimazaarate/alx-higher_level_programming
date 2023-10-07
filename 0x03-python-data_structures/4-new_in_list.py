#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copied_list = my_list.copy()

    if 0 <= idx < len(my_list):
        my_list[idx] = element
        return my_list
    else:
        return copied_list
