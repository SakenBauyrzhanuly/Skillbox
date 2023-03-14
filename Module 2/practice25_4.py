films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
count_choice = int(input('Сколько фильмов хотите добавить: '))
choice_new = []
for i in range(count_choice):
    choice = input('Введите название фильма: ')
    if choice in films:
        choice_new.append(choice)
    else:
        print('Фильма ', choice,'у нас нет :(')
print('Ваш список любимых фильмов: ',choice_new)