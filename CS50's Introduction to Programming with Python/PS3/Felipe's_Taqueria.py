# Felipe’s Taqueria
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0
ordered = []
while True:
    for food, price in menu.items():
        print (f'{food} : {price}$')
    order = input("Which item from the menu would you like to order? (press d to stop) ")
    if order in menu:
        total += menu[order]
        ordered.append(order)
        print(f"Total: ${total}")
    elif order == "d":
        print(f"Your total is: ${total} \nItems ordered: {ordered}")
        break
    else:
        print("Wrong input, try again or press d to exit the ordering process!")
