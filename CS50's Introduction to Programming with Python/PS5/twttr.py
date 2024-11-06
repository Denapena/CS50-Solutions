# Just setting up my twttr
def main():
    user_input = input("Input: ")
    print(shorten(user_input))


def shorten(word):
    vowels = ["a","e","i","o","u"]
    response = ""
    for letter in word:
        if letter.lower() not in vowels:
            response += letter
    return response


if __name__ == "__main__":
    main()




