def matrix(arr):
    result = [row[:] for row in arr]  # copy matrix

    for i in range(len(result)):
        if result[i][i] < 0:
            result[i][i] = 0
        else:
            result[i][i] = 1

    return result
