import random


def main():
    level = get_level()
    generate_integer(level)


def get_level():
    while True:
        try:
            level = int(input('Level: '))
        except ValueError:
            pass
        else:
            if 0 < level < 4:
                return level


def generate_integer(level):
    score = 0
    if level == 1:
        min_num = 0
        max_num = 9
    elif level == 2:
        min_num = 10
        max_num = 99
    else:
        min_num = 100
        max_num = 999
    for num in range(10):
        x = random.randint(min_num, max_num)
        y = random.randint(min_num, max_num)

        for i in range(3):
            try:
                answer = int(input(f'{x} + {y} = '))
                if answer != x + y:
                    raise ValueError
                score += 1
                break
            except ValueError:
                print('EEE')
                if i > 1:
                    print(f'{x} + {y} = {x + y}')

    print(f'Score: {score}')


if __name__ == "__main__":
    main()
    # get_level()
