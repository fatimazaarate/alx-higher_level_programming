#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    max_length = max(len(tuple_a), len(tuple_b))
    tuple_a = tuple_a + (0,) * (max_length - len(tuple_a))
    tuple_b = tuple_b + (0,) * (max_length - len(tuple_b))
    
    for i in range(len(tuple_a)):
        new_tuple += (tuple_a[i] + tuple_b[i],)
    return new_tuple
