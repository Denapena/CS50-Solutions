# Vanity Plates

def is_valid(plate):
    punctuations = " _!?.,$#;:-"
    if plate[0:2:].isalpha():
        if 2 <= len(plate) <=6:
            for character in plate:
                if character in punctuations:
                    return False
            for i in range(2,len(plate)):
                if plate[i].isnumeric() and plate[i] != "0":
                    if plate[i::].isnumeric():
                        return True
                    else:
                        return False
                elif plate[i] == "0":
                    return False
            return True
    return False


print(is_valid("A1BC23"))
print(is_valid("AABC23453"))
print(is_valid("AAASD?"))
print(is_valid("AABC23"))
print(is_valid("AAC23D"))
print(is_valid("AABC23"))
print(is_valid("AAB023"))