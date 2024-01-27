def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # if len(s) < 2 or len(s) > 6:
    #     return False
    if not s.isalnum() or not s[0:2].isalpha():
        return False
    if nums := get_nums(s[2:]):
        if not nums.isdigit() or nums.startswith('0'):
            return False
    return True


def get_nums(s):
    for c in s:
        if c.isdigit():
            return s[s.index(c):]
    return ''


if __name__ == "__main__":
    main()
