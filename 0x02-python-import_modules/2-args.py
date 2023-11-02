#!/usr/bin/python3
if __name__ == "__main__":
    """printing command line arguments"""
    from sys import argv

    count = len(argv)
    delim = ":"

    if count == 1:
        delim = "."
        count = 0
        print("{} arguments{}".format(count, delim))
    elif count == 2:
        print("{} argument{}".format(count - 1, delim))
    else:
        print("{} arguments{}".format(count - 1, delim))

    for i in range(1, count):
        print("{}{} {}".format(i, delim, argv[i]))
