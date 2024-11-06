import sys

count=0

if len(sys.argv) < 2:
    sys.exit("Too few arguments!")
elif len(sys.argv) >2:
    sys.exit("Too many arguments!")


if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file!")
else:
    try:
        with open(sys.argv[1],"r") as file:
            for row in file:
                if row.lstrip().startswith("#") or not row.strip():
                    continue
                count += 1
        sys.exit(f"File {sys.argv[1]} contains {count} lines of code!")
    except FileNotFoundError:
        sys.exit("File does not exist!")