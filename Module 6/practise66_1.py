violator_songs = {
'World in My Eyes': 4.86,
'Sweetest Perfection': 4.43,
'Personal Jesus': 4.56,
'Halo': 4.9,
'Waiting for the Night': 6.07,
'Enjoy the Silence': 4.20,
'Policy of Truth': 4.76,
'Blue Dress': 4.29,
'Clean': 5.83
}
# times = 3
# res_summ = 0
# for i_times in range(times +1):
#     name_music = input('Название первой песни: ')
#     if name_music in violator_songs:
#         res_summ += (violator_songs.get(name_music))
# print(res_summ)

def find_dict(string_i):
    for i, j in violator_songs.items():
        if i == string_i:
            return j
    else:
        print('Нет в словаре')



res_summ = 0
times = 3
for i_times in range(times):
    name_music = input('Название песни: ')
    res_summ += find_dict(name_music)
print(res_summ)


