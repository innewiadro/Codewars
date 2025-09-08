def digits(num):
    digs = [int(d) for d in str(num)]
    result = []
    for i in range(len(digs)):
        for j in range(i+1, len(digs)):
            result.append(digs[i] + digs[j])
    return result
