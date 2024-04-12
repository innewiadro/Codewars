def well(x):
    a = 0
    for i in x:
        if i == "good":
            a += 1
    if a > 2:
        return "I smell a series!"
    elif a >= 1:
        return 'Publish!'
    return 'Fail!'
