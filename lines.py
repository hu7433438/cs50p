import sys
argv_len = len(sys.argv)
if argv_len == 1:
    sys.exit("Too few command-line arguments")
elif argv_len > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")
else:
    try:
        with open(sys.argv[1]) as f:
            a = 0
            for line in f.readlines():
                if line and not line.lstrip().startswith('#') and not line.isspace():
                    # print(line)
                    a += 1
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        print(a)
