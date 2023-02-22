def stray(arr):
    for number in arr:
        arr.count(number)
        print(arr.count(number))
        if arr.count(number) == 1:
            return number
