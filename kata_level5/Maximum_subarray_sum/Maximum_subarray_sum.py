def max_sequence(arr):
    maximum = 0
    local = 0
    for i in arr:
        if local > 0:
            local += i
            if local < 0:
                local = 0
            elif local > maximum:
                maximum = local
        elif i > 0:
            local += i
            print(local)

    return maximum
