#!/usr/bin/python3
"""is_same_class"""


def is_same_class(obj, a_class):
    """return true if obj is the exact cls a_class,
    otherwise false
    """

    return (type(obj) == a_class)
