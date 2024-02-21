def logical_calc(array, op):
    print(array, op)
    res = array[0]
    for i in array[1:]:
        if op == "AND":
            res = res & i
        if op == "OR":
            res = res | i
        if op == "XOR":
            res = res ^ i
    return res
