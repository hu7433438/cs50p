# while True:
#     f = input('Fraction: ').strip()
#     try:
#         x, y = map(int, f.split('/'))
#         percentage = round(x / y * 100)
#     except (ValueError, ZeroDivisionError):
#         pass
#     else:
#         if 0 <= percentage <= 100:
#             if percentage < 2:
#                 print('E')
#             elif percentage > 98:
#                 print('F')
#             else:
#                 print(f'{percentage}%')
#             break


def main():
    f = input('Fraction: ').strip()
    print(gauge(convert(f)))


def convert(fraction):
    x, y = map(int, fraction.split('/'))
    a = round(x / y * 100)
    if a > 100 or x > y:
        raise ValueError
    return a


def gauge(percentage):
    if percentage < 2:
        return 'E'
    elif percentage > 98:
        return 'F'
    else:
        return f'{percentage}'


if __name__ == "__main__":
    main()
