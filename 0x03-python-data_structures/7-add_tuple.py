#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """Add two tuples or default 0"""
    tuple_a = tuple_a[:2] + (0, 0) if len(tuple_a) < 2 else tuple_a[:2]
    tuple_b = tuple_b[:2] + (0, 0) if len(tuple_b) < 2 else tuple_b[:2]
    """Return a tuple with the sum of corresponding elements"""
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
