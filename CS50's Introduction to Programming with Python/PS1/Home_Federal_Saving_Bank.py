# Home Federal Savings Bank
greeting = input("Hello there:  ")

if greeting.strip().lower() == "hello":
    print("$0")
elif greeting.strip().lower()[0] == "h":
    print("$20")
else:
    print("$100")