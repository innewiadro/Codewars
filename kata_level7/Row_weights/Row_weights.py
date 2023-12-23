def row_weights(array):
    left = 0
    right = 0
    counter = 0
    for i in array:
        if counter % 2 == 0:
            left += i
        else:
            right += i
        counter += 1

    return left, right
