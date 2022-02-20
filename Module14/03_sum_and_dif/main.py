def summ_number(x):
    summ_n = 0
    while x != 0:
        digital = x % 10
        summ_n += digital
        x //= 10
    print(f'Сумма цифр: {summ_n}')
    return summ_n


def number(x):
    count = 0
    while x != 0:
        x //= 10
        count += 1
    print(f'Кол-во цифр в числе: {count}')
    return count


x = int(input('Введите число: '))
print('Разность суммы и кол-ва цифр: ', summ_number(x) - number(x))

# зачтено
