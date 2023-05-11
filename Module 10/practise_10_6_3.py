import re


def check_len(data):
    try:
        if len(data) < 3:
            raise IndexError
    except IndexError:
        comment_1 = 'НЕ присутствуют все три поля:\n'
        bad_log(data, comment_1)


def find_name(my_str):
    try:
        if not my_str.isalpha():
            raise NameError
    except NameError:
        comment_1 = 'Поле «Имя» содержит НЕ только буквы\n'
        bad_log(my_str, comment_1)
        return True
    return False

def correct_mail(email):
    try:
        regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if not (re.search(regex, email)):
            raise SyntaxError
    except SyntaxError:
        comment_1 = 'Поле «Имейл» НЕ содержит @ и точку\n'
        bad_log(email, comment_1)
        return True
    return False

def test_ages(my_num):
    try:
        if not 10 < my_num < 99:
            raise ValueError
    except ValueError:
        comment_1 = 'Поле «Возраст» НЕ представляет число от 10 до 99\n'
        bad_log(my_num, comment_1)
        return True
    return False

def bad_log(error_info, comments):
    with open('registrations_bad.log', 'a', encoding='utf') as error_file:
        error_file.write(str(error_info) + '\n' + comments)


def good_log(good_info):
    with open('registrations_good.log', 'a', encoding='utf') as good_file:
        good_file.write(good_info)


def main():
    with open('registrations.txt', 'r', encoding='utf') as reg_file:
        for i_str in reg_file:
            words = i_str.split(' ')

            if len(words) < 3:
                check_len(words)
                continue
            else:
                name, email, ages = words
                age_r = ages.strip()

            test_name = find_name(name)
            test_mail = correct_mail(email)
            test_age = test_ages(int(age_r))

            if test_age or test_mail or test_name:
                pass
            else:
                good_log(i_str)


main()

# if test_ages(int(age)) is True:
#     print('Поле «Возраст» представляет число от 10 до 99')
# else:
#     print('Поле «Возраст» НЕ представляет число от 10 до 99')
#
#
#
# if correct_mail(email) is True:
#     print('Поле «Имейл» содержит @ и точку')
# else:
#    print('Поле «Имейл» НЕ содержит @ и точку')
#
#
# if correct_mail(name) is True:
#     print('Поле «Имя» содержит только буквы.')
# else:
#    print('Поле «Имя» содержит НЕ только буквы')
#
#
# if find_field(i_str) is True:
#     print('Присутствуют все поля\n')
# else:
#    print('НЕ присутствуют все три поля\n')
# print(i_str)

# write_files = open('registrations_good.log', 'w', encoding='utf')
#     write_files.write()
#     write_files.close()
