def bingo(array):
    target_array = [2, 9, 14, 7, 15]

    if all(num in array for num in target_array):
        return "WIN"
    else:
        return "LOSE"
