skates = int(input('Количество коньков: '))
skate_list = []
people_list = []
for i_skate in range(skates):
    print('Размер пары', i_skate + 1, ': ')
    size_skate = int(input())
    skate_list.append(size_skate)
print(skate_list)
people = int(input('Количество людей: '))
for i_people in range(people):
    print('Размер ноги человека', i_people + 1, ': ')
    size_people = int(input())
    people_list.append(size_people)
print(people_list)
count = 0
for i in range(len(skate_list)):
    if skate_list[i] in people_list:
        count += 1
print('Наибольшее количество людей, которые могут взять ролики: ',count)