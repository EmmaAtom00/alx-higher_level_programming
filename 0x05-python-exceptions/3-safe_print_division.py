#!/usr/bin/python3
def safe_print_division(a, b):
    """Divides 2 integers and print the result
    Args:
        a (int): The first integer
        b (int): The second integer
    Return:
        Return the result of the division otherwise none
    """
    result = 0
    try:
        quotient = a/b
        result = quotient
        return (quotient)
    except (ZeroDivisionError, TypeError, ValueError):
        return ("None")
    finally:
        print("Inside result: {}".format(result))
