# Fuel Gauge
def fuel_level():
    while True:
        try:
            fraction = (input("Fraction: "))
            x, y = fraction.split('/')
            return int(x)/int(y)*100
        except ValueError:
            print("ValueError ocurred.")
        except ZeroDivisionError:
            print("You cannot divide with zero.")
        except Exception as e:
            print(f"Error has happened: {e}")

x = fuel_level()

if 99 <= x <= 100:
    print("F")
elif 0 <= x <= 1:
    print("E")
elif 1 < x < 99:
    print(f"{x}%")
else:
    print("Wrong input!")