def ceaser_chipher(string, user_shift):
    char_list = [(alphabet[(alphabet.index(sym) + user_shift) % 33] if sym != ' ' else ' ') for sym in string]
    new_str = ''
    for i_char in char_list:
        new_str += i_char
    return new_str

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
input_str = input('Введите строку: ')
shift = int(input('Введите сдвиг: '))

output_str = ceaser_chipher(input_str, shift)
print('Зашифрованная строка: ', output_str)


print(ord("а"), ord("я"), ord("ё"), chr(1104))

text = input("Введите текст: ")
delta = int(input("Введите сдвиг: "))
alphabet = [chr(index) for index in range(ord("а"), ord("я") + 1)]  # заполняем список буквами алфавита
# Думаем над структурой алгоритма: [вариант_1 если условие_1 иначе вариант_2 for буква in текст]
new_text = [alphabet[(alphabet.index(letter) + delta) % len(alphabet)] if letter in alphabet else letter for letter in text.lower()]
print(''.join(new_text))