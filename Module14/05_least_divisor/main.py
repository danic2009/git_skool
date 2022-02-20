def dell(a):
    b = a - 1
    while a % b != 0:
        b = b - 1
    if a % b == 0:
        b = a // b
    print(b)


a = int(input('Введите число: '))
dell(a)

# зачтено
