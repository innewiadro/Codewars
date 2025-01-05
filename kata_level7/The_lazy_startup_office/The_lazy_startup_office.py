def bin_rota(arr):
    rota = []
    for i, row in enumerate(arr):
        if i % 2 == 0:
            rota.extend(row)
        else:
            rota.extend(reversed(row))
    return rota
