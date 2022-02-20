def find(x, y, r):
    if x <= r and y <= r:
        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет')


print('Введите координаты монетки:')
x = float(input('x '))
y = float(input('y '))
r = int(input('Введите радиус: '))

if x < 0 or y < 0 or r < 0:
    print('Данные не могут быть меньше 0')
else:
    find(x, y, r)

# зачтено
