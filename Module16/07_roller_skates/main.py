size_skates = []  # Размер коньков
size_peopl = []  # Размер ног
size_peopl.sort()
size_skates.sort()
skates = int(input('Кол-во коньков: '))
for i in range(skates):
    size_skates.append(int(input(f'Размер {i + 1} пары: ')))
peopl = int(input('\nКол-во людей: '))
for i in range(peopl):
    size_peopl.append(int(input(f'Размер ноги {i + 1} человека:')))

count = 0

for i in size_skates:
    for j in size_peopl:
        if i >= j:
            count += 1
            size_peopl.remove(j)

print(f'\nНаибольшее кол-во людей, которые могут взять ролики: {count}')

# зачтено
