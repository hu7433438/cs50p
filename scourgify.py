import csv
import sys


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    # for arg in sys.argv[1:]:
    #     if not arg.endswith(".csv"):
    #         sys.exit("Not a CSV file")
    try:
        with open(sys.argv[1]) as f:
            reader = csv.DictReader(f)
            table = []
            for row in reader:
                last, first = row["name"].split(",")
                table.append({"first": first.lstrip(), "last": last, "house": row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
    else:
        with open(sys.argv[2], "w", newline='') as f:
            fieldnames = ["first", "last", "house"]
            # writer = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(table)
            # for row in table:
            #     writer.writerow(row)
