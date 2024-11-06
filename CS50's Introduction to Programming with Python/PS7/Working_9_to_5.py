import re

def convert(str):
    if x:= re.search(r"^([0-1]?[0-9]|1[0-1]):?([0-5][0-9])?\s([AP][M])\sto\s([0-1]?[0-9]|1[0-1]):?([0-5][0-9])?\s([AP][M])$",str,re.IGNORECASE):
        group1 = x.group(1)
        group2 = x.group(2)
        group3 = x.group(3)
        group4 = x.group(4)
        group5 = x.group(5)
        group6 = x.group(6)
        if group2 == None:
            group2 = "00"
        if group5 == None:
            group5 = "00"
        if group3 == "AM" and group6 == "AM":
            time = f"{group1}:{group2} to {group4}:{group5}"
        elif group3 == "AM" and group6 == "PM":
            group4 = (int(group4)+12)
            time = f"{group1}:{group2} to {group4}:{group5}"
        else:
            group1 = (int(group1)+12)
            group4 = (int(group4)+12)
            time = f"{group1}:{group2} to {group4}:{group5}"
        print(time)
    else:
        raise ValueError
    

convert("9:00 AM to 5:00 PM")
convert("9 AM to 5 PM")
convert("9:00 AM to 5 PM")
convert("9 AM to 5:00 PM")
convert("9 AM to 5:00 PM")
convert("9 AM to 11:00 AM")
convert("2 PM to 5:00 PM")