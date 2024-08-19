def paint_letterboxes(start, finish):
    digit_counts = [0] * 10
    for i in range(start, finish + 1):
        for digit in str(i):
            digit_counts[int(digit)] += 1

    return digit_counts
