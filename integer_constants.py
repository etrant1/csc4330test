import re

str = input("Enter integer constant or enter 'stop': ")
while (str != "stop"):
    if (re.search("^(?!.* .*)(0|0x|Ox|[1-9]).+", str) != None):
        if (re.search("^[1-9]", str)):
            print("Decimal")
        elif (re.search("^(0x|Ox|oX).+", str)):
            print("Hexadecimal")
        elif (re.search("^0.+", str)):
            print("Octal")
        else:
            print("Invalid")
    else:
        print("Invalid")

    str = input("Enter integer constant or enter 'stop': ")

