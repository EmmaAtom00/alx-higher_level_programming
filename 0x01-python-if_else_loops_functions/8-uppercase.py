#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in str:
        Alpnum = ord(i)
        if Alpnum >= 97 and Alpnum <= 122:
            Alpnum = Alpnum - 32
        result += chr(Alpnum)
    print("{}".format(result))
