def func() -> None:
    print('Я - функция func() из test_module.py, и я что то делаю')


if __name__ == '__main__':
    print('Здесь какой то основной код')
    func()
else:
    print('Импортирован модуль', __name__)

