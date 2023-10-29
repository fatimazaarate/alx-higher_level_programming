#!/usr/bin/python3
'''
Module for text_indentation method
it prints a text with 2 new lines after each of these characters: ., ? and :
returns nothing
'''


def text_indentation(text):
    '''
    Function prints a that text with 2 new lines.
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] in [".", "?", ":"]:
            print("{}\n".format(text[i]))
        elif text[i] == " " and text[i - 1] in [".", "?", ":"]:
            continue
        else:
            print("{}".format(text[i]), end="")
