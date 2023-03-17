N_team = int(input('Количество участников: '))
M_team = int(input('Количество человек в команде: '))
team = []
n = 1
for i in range(N_team // M_team):
    team.append(list(range(n,n + M_team)))
    n += M_team
print(team)


# N = int(input('Количество участников: '))
# members = []
# num = 1
# for _ in range(N // 3):
#     members.append(list(range(num,num + 3)))
#     num += 3
#
# print(members)