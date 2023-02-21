import re

str = input("Enter floating-point constant or enter 'stop': ")
while (str != "stop"):
    if (re.search("^(?!.* .*)-?[0-9]+.?[0-9]*[eE]?-?[0-9]+[fFlL]*", str) == None):
        print(str + " is INVALID")
    elif (re.search("[fF]$", str)):
        print(str + " is VALID <float>")
    else:
        print(str + " is VALID <double>")
    str = input("Enter floating-point constant or enter 'stop': ")

