def year(start, stop):
    for i in range(start, stop + 1):
        x = i
        a = x % 10
        x //= 10
        b = x % 10
        x //= 10
        c = x % 10
        x //= 10
        d = x % 10
        if a == b == c or b == c == d or c == d == a or a == b == d:
            print(i)


start = int(input('Введите первый год: '))
stop = int(input('Введите второй год:'))
print()

if start > stop:
    print('Первый год не может быть больше второго')
elif start < 1000 or stop >= 10000:
    print('Год должен быть 4-х значным.')
else:
    print(f'Года от {start} до {stop} с тремя одинаковыми цифрами:')
    year(start, stop)

# зачтено
