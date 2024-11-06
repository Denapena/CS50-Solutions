# Adieu, Adieu

def adieu():
    names = []
    bye = "Adieu, adieu, to "
    while True:
        name = input("Name (press d to stop adding them): ")
        if name.lower() == "d":
            break
        else:
            names.append(name)
    for name in names:
        bye += name
        print(bye)
        bye = bye.replace(" and ",", ")
        bye += " and "
        
adieu()
