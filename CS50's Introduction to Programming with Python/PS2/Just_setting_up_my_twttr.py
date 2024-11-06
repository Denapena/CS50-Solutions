# Just setting up my twttr

user_input = input("Input: ")
response = ""

for letter in user_input:
    if letter.lower() not in ["a","e","i","o","u"]:
        response += letter

print(response)
