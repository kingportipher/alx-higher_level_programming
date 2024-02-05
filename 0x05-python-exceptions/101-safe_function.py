#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    """Executes a function safely.
    Args:
        fct: The function to execute
        Args: Arguments for fct
    Return:
        If an error occurs - None.
        Otherwise - the result of the call to fct.
    """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[i]), file=sys.stderr)
        return (None)
