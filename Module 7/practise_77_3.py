players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}
result = [(last_first[0], last_first[1], *pairs) for last_first, pairs in players.items()]

# for last_first, pairs in players.items():
#     result[last_first] = pairs[0], pairs[1], pairs[2]
print(result)