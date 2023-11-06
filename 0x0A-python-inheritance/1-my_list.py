#!/usr/bin/python3
"""
a class MyList that inherits from list
"""


class MyList(list):
    """
        Sorts the elements of the list instance in ascending order and prints the sorted result.

        Parameters:
        None

        Returns:
        None

        Example Usage:
        my_list = MyList([4, 2, 1, 3, 5])
        my_list.print_sorted()  # Prints the sorted list: [1, 2, 3, 4, 5]
        """

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
