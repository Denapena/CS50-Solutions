# Coke Machine

price = 50

while price > 0:
    print("Amount due:",price,"cents")
    coin = int(input("Insert a coin: "))
    if coin not in [25,10,5]:
        print("The machine only accepts 25 cents, 10 cents or 5 cents.")
        continue
    price -= coin
    if price <= 0:
        print("Change owed:",0-price,"cents")