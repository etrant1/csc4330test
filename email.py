import re

str = input("Enter string input or enter 'stop': ")
while (str != "stop"):
    # pattern checking the username and the domain seperately
    address_list = str.split("@")
    if re.search("^(?!\.|.*\.\.)[a-zA-Z0-9#!%$‘&+*–/=?^_`.{|}~]+[a-zA-Z0-9#!%$‘&+*–/=?^_`{|}~]$",
                 address_list[0]) == None:
        print("Invalid email address")
    elif re.search("^(?!-|.*\.\.|\.$|-$)[a-zA-Z0-9.-]+\.[a-zA-Z0-9.]+$", address_list[1]) == None:
        print("Invalid email address")
    else:
        print("String is a valid email address")
    str = input("Enter string input or enter 'stop': ")
