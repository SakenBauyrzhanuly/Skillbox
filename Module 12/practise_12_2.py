# В данном коде мы создаем логгер с именем файла 'karma.log'
# и уровнем логирования 'ERROR', а также создаем 5 классов исключений для возможных ошибок.
# Далее, мы определяем функцию one_day(),
# которая генерирует случайное число для кармы и может с некоторой вероятностью выбросить одно из исключений.
#
# Затем, мы запускаем бесконечный цикл, в котором вызываем функцию one_day() и пытаемся увеличить карму.
# Если происходит одно из исключений, мы записываем его в лог.
# Когда карма достигнет 500, цикл прервется и мы закроем файл лога.

import random


class KillError(Exception):
    def __str__(self):
        return 'KillError'


class DrunkError(Exception):
    def __str__(self):
        return 'DrunkError'


class CarCrashError(Exception):
    def __str__(self):
        return 'CarCrashError'


class GluttonyError(Exception):
    def __str__(self):
        return 'GluttonyError'


class DepressionError(Exception):
    def __str__(self):
        return 'DepressionError'


def one_day():
    error = ''
    try:
        karma = (random.randint(1, 7))
        if random.randint(1, 10) == 1:
            error = random.choice([KillError, DrunkError, CarCrashError, GluttonyError, DepressionError])
            raise error
        return karma

    except error:
        with open('karma.log', 'a', encoding='utf-8') as karma_errors:
            karma_errors.write(str(error) + '\n')


karma_end = 0
while karma_end < 500:
    karma = one_day()
    if isinstance(karma, int):
        karma_end += karma


# numbers_file.close()

print(karma_end)
