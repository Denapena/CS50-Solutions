# Little Professor

from random import randint

def main():
    score = 0
    level = get_level()
    print(f"Level {level}")
    for i in range(10):
        attempt = 0
        question = generate_integer(level)
        while True:
            answer = input(question)
            if answer == str(z):
                score += 1
                break
            else:
                attempt +=1
                if attempt == 3:
                    print(question + str(z))
                    break
    print(f"Score: {score}")

        
def get_level():
    while True:
        try:
            level = int(input("Select the desired level (1-3): "))
            if 1 <= level <= 3:
                return level
            else:
                print("Wrong input, number 1-3 needed.")
        except ValueError:
            print("Wrong input, number 1-3 needed.")


def generate_integer(level):
    global z
    x = randint (1,level*10)
    y = randint (1,level*10)
    z = x+y
    return f"{x} + {y} = "


if __name__ == "__main__":
    main()