def well(arr):
    res = 0
    for i in arr:
        for j in i:
            if isinstance(j, str) and j.lower() == "good":
                res += 1
    if res == 0:
        return "Fail!"
    elif res < 3:
        return "Publish!"
    else:
        return "I smell a series!"
