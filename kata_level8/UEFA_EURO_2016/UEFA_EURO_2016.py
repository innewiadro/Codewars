def uefa_euro_2016(teams, scores):
    if scores[0] > scores[1]:
        winner = teams[0] + " won!"
    elif scores[0] < scores[1]:
        winner = teams[1] + " won!"
    else:
        winner = "teams played draw."

    return f"At match {teams[0]} - {teams[1]}, {winner}"
