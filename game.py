import random

while True:
    try:
        i = int(input("Level:"))
    except ValueError:
        pass
    else:
        if i > 0:
            level = random.randint(1, i)
            break

while True:
    try:
        g = int(input("Guess: "))
    except ValueError:
        pass
    else:
        if g > level:
            print('Too large!')
        elif g < level:
            print('Too small!')
        else:
            print('Just right!')
            break
