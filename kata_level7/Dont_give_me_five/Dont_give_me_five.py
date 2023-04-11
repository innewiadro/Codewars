def dont_give_me_five(start, end):
    a = []
    for i in range(start, end+1):
        if '5' not in str(i):
            a.append(i)

    return len(a)
