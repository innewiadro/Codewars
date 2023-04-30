def parts_sums(ls):

    if not ls:
        return [0]

    new_list = []
    total = sum(ls)
    new_list.append(total)

    for i in ls:
        total -= i
        new_list.append(total)
    
    return new_list
