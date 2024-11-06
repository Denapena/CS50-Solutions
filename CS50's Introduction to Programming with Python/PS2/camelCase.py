# camelCase

name = input("camelCase: ")

snake = ""

for letter in name:
    if letter.isupper():
        letter = "_" + letter.lower()
    snake += letter

print(snake)
