while True:
    password = input('Придумайте пароль: ')

    apper = any([1 if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' else 0 for i in password])
    lower = any([1 if i in 'bcdefghijklmnopqrstuvwxyz' else 0 for i in password])
    digits = any([1 if i in '1234567890' else 0 for i in password])
    len_digits = False
    count_len_digit = 0

    for i_digit in password:
        if i_digit.isdigit():
            count_len_digit += 1
        if count_len_digit >= 3:
            len_digits = True

    if len(password) >= 8 and apper and lower and digits and len_digits:
        print('Это надёжный пароль!')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')

