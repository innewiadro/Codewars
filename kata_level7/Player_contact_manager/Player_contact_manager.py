def player_manager(players):
    if not players:
        return []

    data = players.split(", ")
    result = []

    for i in range(0, len(data), 2):
        result.append({
            "player": data[i],
            "contact": int(data[i + 1])
        })

    return result
