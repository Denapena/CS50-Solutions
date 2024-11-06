# Fuel Gauge
def main():
    fraction = input("Fraction: ")
    print(gauge(convert(fraction)))


def convert(fraction):
    while True:
        try:
            fraction = fraction.split("/")
            return int(fraction[0])/int(fraction[1])*100
        except ValueError:
            print("ValueError ocurred.")
        except ZeroDivisionError:
            print("You cannot divide with zero.")
        except TypeError:
            print("TypeError ocurred.")
        except Exception as e:
            print(f"Error has happened: {e}")


def gauge(percentage):
    if 99 <= percentage <= 100:
        return "F"
    elif 0 <= percentage <= 1:
        return "E"
    elif 1 < percentage < 99:
        return f"{percentage}%"
    else:
        return "Wrong input!"


if __name__ == "__main__":
    main()

