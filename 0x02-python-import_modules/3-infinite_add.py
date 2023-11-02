#!/usr/bin/python3
if __name__ == "__main__":
    """Print the result of adding two arguments"""
    from sys import argv

    count = len(argv)
    if count == 1:
        print(0)
    else:
        if count == 2:
            print(argv[1])
        else:
            result = argv[1]
            for i in range(2, count):
                result = int(result) + int(argv[i])
            print(result)
