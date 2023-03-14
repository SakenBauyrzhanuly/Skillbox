count_video = int(input('Количество видеокарт: '))
old_card = []
new_card = []
maximum = 0

for i in range(0, count_video):
    print('Видеокарта ', i + 1, ': ')
    vid_card = int(input())
    old_card.append(vid_card)
    if maximum <= vid_card:
        maximum = vid_card
    else:
        new_card.append(vid_card)
print('Новый список видеокарт: ', new_card)
print('Старый список видео карт: ', old_card)

