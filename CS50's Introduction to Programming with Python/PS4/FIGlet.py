# Frank, Ian and Glen’s Letters

import sys
from pyfiglet import Figlet
from random import choice

figlet = Figlet()


if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        try:
            figlet.setFont(font=sys.argv[2])
        except KeyError:
            sys.exit("Invalid font name")
        text = input("Input: ")
        print(figlet.renderText(text))
    else:
        sys.exit("Wrong input!")
elif len(sys.argv) == 1:
    random_font = choice(figlet.getFonts())
    figlet.setFont(font=random_font)
    text = input("Input: ")
    print(figlet.renderText(text))
else:
    sys.exit("Not the right amount of arguments!")

