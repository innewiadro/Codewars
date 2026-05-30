def distribution_of(golds):
    left = 0
    right = len(golds) - 1

    a = 0
    b = 0
    turn_a = True

    while left <= right:
        if golds[left] >= golds[right]:
            take = golds[left]
            left += 1
        else:
            take = golds[right]
            right -= 1

        if turn_a:
            a += take
        else:
            b += take

        turn_a = not turn_a

    return [a, b]
