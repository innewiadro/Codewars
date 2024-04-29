def balance(left, right):
    weight = {'!': 2, '?': 3}
    left_score = 0
    right_score = 0
    for i in left:
        left_score += weight[i]
    for j in right:
        right_score += weight[j]
    return "Right" if right_score > left_score else "Balance" if right_score == left_score else "Left"
