# Home Federal Savings Bank
def main():
    greeting = input("Hello there:  ")
    print(value(greeting))

def value(greeting):
    if greeting.strip().lower() == "hello":
        return "$0"
    elif greeting.strip().lower()[0] == "h":
        return "$20"
    else:
        return "$100"
    ...


if __name__ == "__main__":
    main()