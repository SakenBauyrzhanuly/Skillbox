import random
team_1 = [round(random.uniform(0, 10), 2) for i in range(20)]
team_2 = [round(random.uniform(0, 10), 2) for j in range(20)]

war = [round(team_1[i], 2) if team_1[i] > team_2[i] else round(team_2[i], 2)
       for i in range(20)]

print(team_1)
print(team_2)
print(war)