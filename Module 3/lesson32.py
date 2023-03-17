# langs = ['Python', 'Java', 'JS', 'SQL']
# user_lang = input('После чего ставить: ')
# i_lang = langs.index(user_lang)
#
# langs.insert(i_lang + 1, 'C++')
# print(langs)


def  is_film_exist(movie, films_list):
    for i_movie in films_list:
        if i_movie == movie:
            return True
    return False




print('Rating films')
films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']

my_list = []

while True:
    print('\nВаш текущий топ фильмов: ', my_list)
    new_movie = input('Название фильма : ')
    if is_film_exist(new_movie, films):
        print('Комады: добавить, удалить, вставить')
        command = input('Введите команду: ')
        if command == 'Добавить':
            my_list.append(new_movie)
        if command == 'Удалить':
            if is_film_exist(new_movie,my_list):
                my_list.remove(new_movie)
            else:
                print('Такого фильма нет в нашем рейтинге.')
        if command == 'Вставить':
            index = int(input('На какое место: '))
            my_list.insert(index - 1, new_movie)
    else:
        print('Такого фильма нет на сайте. ')