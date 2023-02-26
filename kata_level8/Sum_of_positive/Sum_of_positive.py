def positive_sum(arr):
    b = []
    for i in arr:
        if i > 0:
            print(b)
            b.append(i)

    return 0 if len(b) == 0 else sum(b)
