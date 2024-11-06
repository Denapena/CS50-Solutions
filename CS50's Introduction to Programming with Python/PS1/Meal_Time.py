# Meal Time
def main():
    time = input("What is the time? ")
    adj_time = convert(time)
    if 7.0 <= adj_time <=8.0:
        print("Breakfast time")
    elif 12.0 <= adj_time <=13.0:
        print("Lunch time")
    elif 18.0 <= adj_time <=19.0:
        print("Dinner time")


def convert(time):
    if len(time) != 5:
        time = "0"+time
    last_digits = str(float(time[3::])/60)
    time = time.replace(time[2::1],last_digits[1::])
    print(time)
    return float(time)


if __name__ == "__main__":
    main()
