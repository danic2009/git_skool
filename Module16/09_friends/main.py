frends = int(input('Кол-во друзей: '))
dolg = int(input('Долговых расписок: '))

frends_list = []

for _ in range(frends):
    frends_list.append(0)

for i in range(dolg):
    print(f'\n{i + 1} расписка')
    who = int(input('Кому: '))
    from_who = int(input('От кого: '))
    houmach = int(input('Сколько: '))
    frends_list[from_who - 1] += houmach
    frends_list[who - 1] -= houmach
print(f'\nБаланс друзей: ')
for i in range(len(frends_list)):
    print(i + 1, ": ", frends_list[i])

# зачтено
