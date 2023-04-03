player_dict = {
    1: {'name': 'Vanya', 'team':'A', 'status': 'Rest'},
    2: {'name': 'Lanya', 'team':'B', 'status': 'Training'},
    3: {'name': 'Sanya', 'team':'C', 'status': 'Travel'},
    4: {'name': 'Danya', 'team':'C', 'status': 'Rest'},
    5: {'name': 'Ranya', 'team':'A', 'status': 'Training'},
    6: {'name': 'Banya', 'team':'A', 'status': 'Rest'},
    7: {'name': 'Manya', 'team':'B', 'status': 'Rest'},
    8: {'name': 'Ganya', 'team':'C', 'status': 'Travel'},
}

team_a_members = [
    player['name']
    for player in player_dict.values()
    if player['team'] == 'A' and player['status'] == 'Rest'
]

print(team_a_members)