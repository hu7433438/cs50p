import csv
import sys

from tabulate import tabulate

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
else:
    try:
        with open(sys.argv[1]) as f:
            reader = csv.DictReader(f)
            table = {}
            name, _ = sys.argv[1].split('.')
            for row in reader:
                table.setdefault(f"{name.title()} Pizza", []).append(row[f"{name.title()} Pizza"])
                table.setdefault('Small', []).append(row['Small'])
                table.setdefault('Large', []).append(row['Large'])
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        print(tabulate(table, headers="keys", tablefmt="grid"))
