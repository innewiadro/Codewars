def sum_of_differences(arr):
    sum_of_list = 0

    if len(arr) > 1:
        a = sorted(arr, reverse=True)

        for i in range(len(a) - 1):
            sum_of_list += a[i] - a[i + 1]

    return sum_of_list
