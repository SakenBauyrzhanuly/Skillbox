violator_songs = [

    ['World in My Eyes', 4.86],

    ['Sweetest Perfection', 4.43],

    ['Personal Jesus', 4.56],

    ['Halo', 4.9],

    ['Waiting for the Night', 6.07],

    ['Enjoy the Silence', 4.20],

    ['Policy of Truth', 4.76],

    ['Blue', 4.29],

    ['Clean', 5.83]

]
# Halo
# Clean
# Blue

choice = int(input('Сколько песен выбрать: '))
summ = 0
for i_ch in range(choice):
    print('Название', i_ch + 1, 'песни: ')
    name = input()
    for i_m in range(len(violator_songs)):
        if violator_songs[i_m][0] == name:
            summ += violator_songs[i_m][1]

print(summ)
