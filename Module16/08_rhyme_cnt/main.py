List_peopl = [i for i in range(1, int(input('Кол-во человек: ')) + 1)]
Number = int(input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {Number} человек')

count = 0  # индекс

for _ in range(len(List_peopl) - 1):
    if count == len(List_peopl):
        count = 0
    else:
        count == count
    start = count % len(List_peopl)
    count = (start + Number - 1) % len(List_peopl)
    print(f'\nТекущий круг людей: {List_peopl}')
    print(f'Начало счёта с номера {List_peopl[start]}')
    print(f'Выбывает человек под номером {List_peopl[count]}')
    List_peopl.remove(List_peopl[count])
print(f'\nОстался человек под номером', *List_peopl)

# зачтено
