import re


def validate(ip):
    if x := re.search(r"^([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])$",ip):
        return True
    else:
        return False


while True:
    IPv4_address = input("IPv4 adress: ")  
    print(validate(IPv4_address))