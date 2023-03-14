list_name = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
app_list = []
for i in range(0, len(list_name), 2):
    print(list_name[i])
    app_list.append(list_name[i])
print(app_list)

