N = int(input('Quantity peolple: '))
number_counter = int(input('what is the number in the counting:'))
print('Then go out number every ', number_counter, 'person')

N_list = []
for i_N in range(1, N + 1):
    N_list.append(i_N)



counter = 0
lenth = 0
while lenth != 1:
    lenth = len(N_list)
    for i in range(lenth):
        counter += 1
        if i == lenth:
            lenth = 0
        if counter == number_counter:
            N_list.remove(N_list[i])
            counter = 0
            print(N_list)
