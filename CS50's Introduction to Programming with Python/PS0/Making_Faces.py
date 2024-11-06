# Making Faces
def convert(x):
    if x == ":)":
        return "🙂"
    elif x == ":(":
        return "🙁"
    else:
        return x
    
def main():
    x = input("Please tell me your mood :) or :( = ")
    print(convert(x))
main()