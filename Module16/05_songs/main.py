violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

count = int(input('Сколько песен выбрать? '))
time_play = 0
for songs in range(count):
    song_name = input(f'Название {songs + 1} песни: ')
    for items in violator_songs:
        if items[0] == song_name:
            time_play += items[1]

print(f'\nОбщее время звучания песен: {round(time_play, 2)}')

# зачтено
