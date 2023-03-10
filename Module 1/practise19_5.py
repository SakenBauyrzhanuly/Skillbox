def colNum(num1, num2):

    while num1 <= num2:
        str_num1 = str(num1)
        cur_var = ''
        sum_var = ''
        for i in range(len(str_num1)):
            current_index_num = str_num1[i]
            if cur_var == current_index_num:
                sum_var += current_index_num
                sum_var += cur_var
            cur_var = current_index_num
        if sum_var.__len__() == 2:
            print(sum_var)

        num1 += 1

colNum(11, 99)