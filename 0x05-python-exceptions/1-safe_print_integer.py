#!/usr/bin/python3

def safe_print_integer(value):
    """Print an integer with "{:d}".format().
    Args:
        value (int): the integer to be printed
    Return:
        Return true if value has been correctly printed, otherwise false
    """

    try:
        print("{:d}".format(value))
        return (True)
    except (ValueError, TypeError):
        return (False)
