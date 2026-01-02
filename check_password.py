def check_the_length(password):
    return len(password) >= 12


def check_digits(password):
    return any (varitable.isdigit() for varitable in password)


def has_upper_letters(password):
    return any (variable.isupper() for variable in password)


def has_letters(password):
    return any (variable.isalpha() for variable in password)


def has_lower_letters(password):
    return any (variable.islower() for variable in password)


def has_symbols(password):
    return any (not variable.isalnum() for variable in password)


def main():
    password = input("Введите пароль: ")
    score = 0

    check_points= [
        (check_the_length, 2),
        (check_digits, 2),
        (has_letters, 2),
        (has_upper_letters, 2),
        (has_lower_letters, 2)
        (has_symbols, 2)
    ]


    for check, points in check_points:
        if check(password):
            score += points

    print("Рейтинг пароля:", score)
    return score


if __name__ == "__main__":
    main()

