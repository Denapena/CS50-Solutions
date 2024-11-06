# Vanity Plates
def main():
    plate = input("Input: ")
    print(is_valid(plate))


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


if __name__ == "__main__":
    main()