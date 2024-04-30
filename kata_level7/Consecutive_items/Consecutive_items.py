def consecutive(arr, a, b):
    counter = 0
    for i in arr:
        if i == a or i == b:
            counter += 1
            if counter == 2:
                return True
        else:
            counter = 0
    return False
