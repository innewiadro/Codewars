def stalin_sort(arr):
    if not arr:
        return

    survivors = [arr[0]]

    for num in arr[1:]:
        if num >= survivors[-1]:
            survivors.append(num)
        else:
            print("Расстрелять!")

    arr[:] = survivors
