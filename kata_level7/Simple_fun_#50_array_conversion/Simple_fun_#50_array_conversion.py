def array_conversion(arr):
    iteration = 1

    while len(arr) > 1:
        new_arr = []

        for i in range(0, len(arr), 2):
            a, b = arr[i], arr[i + 1]
            if iteration % 2 == 1:
                new_arr.append(a + b)
            else:
                new_arr.append(a * b)

        arr = new_arr
        iteration += 1

    return arr[0]
