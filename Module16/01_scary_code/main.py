a = [1, 5, 3]  # Основной
b = [1, 5, 1, 5]  # Превый побочный
c = [1, 3, 1, 5, 3, 3]  # Второй побочный
# for i in b:
#     a.append(i)
# t = 0
# for i in a:
#     if i == 5:
#         t += 1
# print(t)
# d = []
# for i in a:
#     if i != 5:
#         d.append(i)
# for i in c:
#     d.append(i)
# t = 0
# for i in d:
#     if i == 3:
#         t += 1
# print(t)
# print(d)


first_merge = a.count(5) + b.count(5)
print(f'Кол-во цифр 5 при первом объединении: {first_merge}')
second_merge = a.count(3) + c.count(3)
print(f'Кол-во цифр 3 при втором объединении: {second_merge}')
a.extend(b)
for item in a:
    if 5 in a:
        a.remove(5)
a.extend(c)
print(f'Итоговый список: {a}')

# зачтено
