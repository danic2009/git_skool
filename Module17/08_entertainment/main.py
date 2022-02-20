import random

N = ['!' for i in range(int(input('Кол-во палок: ')))]
K = int(input('Кол-во бросков: '))
for shots in range(K):
    L_i = random.randrange(1, 5)
    R_i = random.randrange(5, 10)
    print(f'Бросок {shots + 1}. Сбиты палки с номера {L_i} по номер {R_i}')
    for items in range(L_i - 1, R_i):
        N[items] = '.'

print()
print(N)

# зачтено
