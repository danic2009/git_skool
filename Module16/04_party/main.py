guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

party = True
while party:
    print(f'\nСейчас на вечеринке {len(guests)} человек: {guests}')
    question = input('Гость пришел или ушел? ').lower()
    if question == 'пора спать':
        print('\nВечеринка закончилась, все легли спать.')
        break
    name = input('Имя гостя: ').capitalize()
    print(f'Привет, {name}')
    if question == 'пришел':
        if len(guests) <= 5:
            guests.append(name)
        else:
            print(f'Прости, {name}, но мест нет.')
    elif question == 'ушел':
        print(f'Пока, {name}!')
        guests.remove(name)

# зачтено
