phonebook_dict = {
    ('Петров', 'Ваня') : 88006669698,
    ('Егоров', 'Ваня') : 88006669697,
    ('Сидорова', 'Лена') : 88006669696,
    ('Алексеев', 'Петя') : 88006669695
}

phonebook_dict[('Алексеев', 'Cетя')] = 109090

for i_person in phonebook_dict:
    if 'Сидорова' in i_person:
        print(i_person[1], phonebook_dict[i_person])
print(phonebook_dict)