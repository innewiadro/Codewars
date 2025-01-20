def golf_score_calculator(par_string, score_string):
    res = 0
    score = 0
    for i in par_string:
        res += int(i)

    for j in score_string:
        score += int(j)

    return score - res
