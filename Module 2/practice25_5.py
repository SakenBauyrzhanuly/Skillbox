count_cont = int(input('Количество контейнеров:  '))
choice_old = []
choice_new = []

for i in range(count_cont):
    choice_weight = int(input('Введите вес контейнера: '))
    choice_old.append(choice_weight)
print(choice_old)


new_choice = int(input('Введите вес нового контейнера: '))
count = 0

for el in range(len(choice_old)):
    if new_choice >= choice_old[el]:
        choice_old.insert(el, new_choice)
        count = el
        break

print(choice_old)
print('Номер, который получит новый контейнер: ',count + 1)
