#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divide elements by elemet 2 lists
    Args:
        my_list1 (list): The first list that contains any type
        my_list2 (list): The second list
        list_length (int): The length of both list but can be bigger
    Return:
        Return a new list (length = list_length) with all dividions
    """
    divisionList = []
    for i in range(list_length):
        try:
            div = (my_list_1[i] / my_list_2[i])
        except IndexError:
            print("out of range")
            div = 0
        except (TypeError, ValueError):
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("dividion by 0")
            div = 0
        finally:
            divisionList.append(div)
    return (divisionList)
