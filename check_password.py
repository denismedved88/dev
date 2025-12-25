def has_digit(password):
    if len(password) >= 12:
        print("Пароль достаточно длинный")
        return 2
    print("Пароль короткий")
    return 0


def check_digits(password):
    if any(variable.isdigit() for variable in password):
        print("Пароль содержит цифры")
        return 2
    print("Пароль не содержит цифр")
    return 0


def has_letters(password):
    if any(variable.isalpha() for variable in password):
        print("Пароль содержит буквы")
        return 2
    print("Пароль не содержит букв")
    return 0


def has_upper_and_lower_letters(password):
    has_upper = any(variable.isupper() for variable in password)
    has_lower = any(variable.islower() for variable in password)

    if has_upper and has_lower:
        print("Пароль содержит и большие, и маленькие буквы")
        return 2
    print("Пароль должен содержать буквы разного регистра")
    return 0


def has_symbols(password):
    if any(not variable.isalnum() for variable in password):
        print("Пароль содержит специальные символы")
        return 2
    print("Пароль не содержит специальных символов")
    return 0


def main():
    password = input("Введите пароль: ")
    score = 0

    check_points = [
        has_digit,
        check_digits,
        has_letters,
        has_upper_and_lower_letters,
        has_symbols
    ]

    for check in check_points:
        score += check(password)

    print("Рейтинг пароля:", score)
    return score


if __name__ == "__main__":
    main()
