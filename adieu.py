import inflect
p = inflect.engine()
words = []

while True:
    try:
        words.append(input('Name: '))
    except EOFError:
        print(f"Adieu, adieu, to {p.join(words)}")
        break
