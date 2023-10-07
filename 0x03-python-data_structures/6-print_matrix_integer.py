#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in row:
            print("{:d} " .format(col), end='')
            if col == len(row):
                print(end='')
            else:
                print(" ", end='')
        print()
