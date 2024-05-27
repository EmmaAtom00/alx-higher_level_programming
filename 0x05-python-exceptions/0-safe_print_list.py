#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """ Print x elements of a list.
    Args:
        my_list (list): The list to be printed.
        x (int): The numbers of elements that will be printed.
    Returns:
        The number of elements printed.
    """

    retur = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            retur += 1
        except IndexError:
            break
    print("")
    return (retur)
