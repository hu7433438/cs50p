groceries = {}

while True:
    try:
        item = input().strip()
    except EOFError:
        for k in sorted(groceries):
            print(groceries[k], k.upper())
        break
    else:
        groceries[item] = groceries.get(item, 0) + 1
