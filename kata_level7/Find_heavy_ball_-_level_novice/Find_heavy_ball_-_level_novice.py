def find_ball(scales):
    result = scales.get_weight([0, 1, 2], [3, 4, 5])

    if result == 0:
        result2 = scales.get_weight([6], [7])
        return 6 if result2 == -1 else 7

    elif result == -1:
        result2 = scales.get_weight([0], [1])
        if result2 == 0:
            return 2
        return 0 if result2 == -1 else 1

    else:
        result2 = scales.get_weight([3], [4])
        if result2 == 0:
            return 5
        return 3 if result2 == -1 else 4