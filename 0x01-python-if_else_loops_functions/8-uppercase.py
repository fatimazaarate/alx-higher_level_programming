#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if char >= 'a' and char <= 'z':
            c = chr(ord(char) - 32)
        print('{}' .format(char), end='')
    print()
