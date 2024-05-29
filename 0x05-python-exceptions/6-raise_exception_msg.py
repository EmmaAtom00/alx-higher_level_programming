#!/usr/bin/python3
def raise_exception_msg(message=""):
    """Raise a name exception error message"""
    try:
        raise NameError
    except NameError:
        print(message)
