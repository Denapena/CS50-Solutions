import sys
import csv


if len(sys.argv) < 2:
    sys.exit("Too few arguments!")
elif len(sys.argv) >2:
    sys.exit("Too many arguments!")


if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file!")
else:
    try:
        with open(sys.argv[1],"r") as old, open ("after.csv","w",newline="") as new:
            reader = csv.DictReader(old)
            writer = csv.DictWriter(new,fieldnames=["first","last","house"])
            writer.writeheader()
            for row in reader:
                last, first = row["name"].split(",")
                row_adj = {"first":first.strip(),"last":last.strip(),"house":row.get("house", "")}
                writer.writerow(row_adj)
    except FileNotFoundError:
        sys.exit("File does not exist!")