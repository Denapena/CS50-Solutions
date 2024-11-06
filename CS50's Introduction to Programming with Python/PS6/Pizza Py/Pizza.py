import sys
import tabulate
import csv


if len(sys.argv) < 2:
    sys.exit("Too few arguments!")
elif len(sys.argv) >2:
    sys.exit("Too many arguments!")


if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file!")
else:
    try:
        with open(sys.argv[1],"r") as file:
            reader = csv.reader(file)
            table = []
            headers = []
            for row in reader:
                table.append(row)
            print(tabulate.tabulate(table,headers,tablefmt="grid"))    
    except FileNotFoundError:
        sys.exit("File does not exist!")