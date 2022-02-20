ip = input('Введите IP: ')
split_ip = ip.split('.')
if len(split_ip) < 4:
    print('Адрес - это четыре числа, разделённые точками')
else:
    numeric = 0
    out_of_range = 0
    for numbers in split_ip:
        if numbers.isdigit():
            numeric += 1
            if int(numbers) > 255:
                out_of_range += 1
                print(numbers, 'превышает 255')
        else:
            print(numbers, '- не целое число')
    if out_of_range == 0 and numeric == 4:
        print('IP-адрес корректен')


