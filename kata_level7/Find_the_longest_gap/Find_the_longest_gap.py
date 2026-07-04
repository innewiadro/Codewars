def gap(num):
    binary = bin(num)[2:]
    max_gap = 0
    current_gap = 0
    counting = False

    for char in binary:
        if char == "1":
            if counting:
                max_gap = max(max_gap, current_gap)
            counting = True
            current_gap = 0
        else:
            if counting:
                current_gap += 1

    return max_gap

