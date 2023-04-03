phonebook = {
    'Ваня':100,
    'Петя':300,
    'Алиса':200,

}

other_phonebook = {

    'Таня': 1000,
    'Сетя': 800,
    'Алена': 2000,
}
phonebook.update(other_phonebook)
phonebook['Gosha'] = phonebook.pop('Петя')
print(phonebook)

print(phonebook.get('Таня'))