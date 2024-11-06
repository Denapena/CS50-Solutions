# Grocery List
groc_list = {}
while True:
    grocery = input("Add a grocery to your grocery list: (press d to stop) ")
    if grocery == "d":
        groc_list = dict(sorted(groc_list.items()))
        for keys,values in groc_list.items():
            print(f"{values} : {keys.upper()}")
        break
    elif grocery in groc_list:
        print(f"{grocery} added to your list!")
        groc_list[grocery] += 1
    else:
        groc_list[grocery] = 1
        print(f"{grocery} added to your list!")
