#!/usr/bin/python3
def safe_print_division(a, b):
    """Divides 2 integers and print the result
    Args:
        a (int): The first integer
        b (int): The second integer
    Return:
        Return the result of the division otherwise none
    """

    try:
        quotient = a / b
    except (ZeroDivisionError, TypeError):
        quotient = "None"
    finally:
        print("Inside result: {}".format(quotient))
    return (quotient)
