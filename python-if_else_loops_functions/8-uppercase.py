#!/usr/bin/python3
def uppercase(str):
    uppercase_str = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            uppercase_str = "{:s}{:c}".format(uppercase_str, ord(c) - 32)
        else:
            uppercase_str = "{:s}{:c}".format(uppercase_str, ord(c))
    print("{:s}".format(uppercase_str))
