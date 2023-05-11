# test = 7
#
#
# def f1():
#     # print(test)
#     tesw = 5
#     print(tesw)
#     # test = 5
#     # print(test)
#
#
# def f2():
#     test = 9
#     print(test)
#
#     if 'test' in globals():
#         print('gggg')
#         print(test)
#     if 'test' in locals():
#         print('sss')
#         print(test)
#
#
# f2()
# f1()

def func():
    var = 1

    # def f3():
    #     par = 2
    #     if 'var' not in locals():
    #         raise Exception
    #     print('var' in locals())
    #
    # f3()

    # def f4():
    #     par = 3
    #     print(var)
    #     if 'var' not in locals():
    #         raise Exception

    def f5():
        var = 4
        par = 4
        print(var)
        if 'var' not in globals():
            raise Exception

    f5()


func()
