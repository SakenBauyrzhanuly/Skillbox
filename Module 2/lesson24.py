def length(player_list):
    player_count = 0
    for _ in player_list:
        player_count += 1
    return  player_count


scores = [8, 5, 10, 7, 6]
scores[1] += length(scores)
scores.append(0)
scores[2] += length(scores)

print(scores)