def revers_a(num):
    num = int(num)
    num_r = 0
    while num != 0:
        digit = num % 10
        num = num // 10
        num_r = num_r * 10
        num_r = num_r + digit
    return num_r


def revers_b(num):
    revnum = round(num - int(num), 2) * 100
    revnum = revers_a(revnum) / 100
    return revnum


num_1 = float(input('Введите первое число: '))
num_2 = float(input('Введите второе число: '))
revnum_1a = revers_a(num_1)
revnum_1b = revers_b(num_1)
revnum_2a = revers_a(num_2)
revnum_2b = revers_b(num_2)
revers_1 = revnum_1a + revnum_1b
revers_2 = revnum_2a + revnum_2b
print()
print('Первое число наоборот', revers_1)
print('Второе число наоборот', revers_2)
print('Сумма: ', revers_1 + revers_2)

# зачтено
