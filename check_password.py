def has_digit(password):
    if len(password) >= 12:
        return 2
    return 0


def check_digits(password):
    if any(variable.isdigit() for variable in password):
        return 2
    return 0


def has_upper_letters(password):
    if any(variable.isupper() for variable in password):
        return 2
    return 0

def has_lower_letters(password):
    if any(variable.islower() for variable in password):
        return 2
    return 0


def has_symbols(password):
    if any(not variable.isalnum() for variable in password):
        return 2
    return 0


def main():
    password = input("Введите пароль: ")
    score = 0

    check_points = [
        has_digit,
        check_digits,
        has_upper_letters,
        has_lower_letters,
        has_symbols
    ]

    for check in check_points:
        score += check(password)

    print("Рейтинг пароля:", score)
    return score


if __name__ == "__main__":
    main()
