# Outdated
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
        date = (input("Date: "))
        try:
            adj_date = date.replace(",","").replace("/"," ").split(" ")
            if adj_date[0] in months:
                month = months.index(adj_date[0]) + 1
                day = int(adj_date[1])
                year = adj_date[2]
            else:
                month = int(adj_date[0])
                day = int(adj_date[1])
                year = adj_date[2]
            # Format month and day to always be 2 digits
            print(f"{year}-{month:02}-{day:02}")
        except ValueError:
            print("ValueError ocurred.")
        except Exception as e:
            print(f"Error has happened: {e}")
        

