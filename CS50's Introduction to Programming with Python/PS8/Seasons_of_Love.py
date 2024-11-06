import datetime

def main():
    days = birthday()
    print(f"You are alive for {days} days, {days*24*60} minutes or {days*24*60*60} seconds!")


def birthday():
    birthday = input("Please insert your birthday in the following format YYYY-MM-DD: ")
    today = datetime.datetime.now()
    number_of_days = 0
    year0,month0,day0 = birthday.split("-")
    year0 = int(year0)
    year1,month1,day1 = (str(today)).split("-")
    year1 = int(year1)
    birthday = datetime.datetime.strptime(birthday, '%Y-%m-%d' )
    start = int(birthday.strftime("%j"))
    end = int(today.strftime("%j"))
    for i in range(year1-year0+1):
        year = year0+i
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    if year == year0:
                        number_of_days += 366-start
                    elif year == year1:
                        number_of_days += end
                    else:
                        number_of_days += 366
                else:
                    if year == year0:
                        number_of_days += 365-start
                    elif year == year1:
                        number_of_days += end
                    else:
                        number_of_days += 365
            else:
                if year == year0:
                    number_of_days += 366-start
                elif year == year1:
                    number_of_days += end
                else:
                    number_of_days += 366
        else:
            if year == year0:
                number_of_days += 365-start
            elif year == year1:
                number_of_days += end
            else:
                number_of_days += 365
        print(number_of_days)
    return number_of_days
            
                 

if __name__ == "__main__":
    main()