import random
team_1 = [random.randint(50, 80) for i in range(10)]
team_2 = [random.randint(30, 60) for j in range(10)]

war = ['Погиб' if team_1[i] + team_2[i] > 100 else 'Выжил'
       for i in range(10)]

print(team_1)
print(team_2)
print(war)