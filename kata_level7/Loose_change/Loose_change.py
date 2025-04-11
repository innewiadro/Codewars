def change_count(change_str):
    total = 0
    for coin in change_str.split():
        total += CHANGE.get(coin, 0)
    return "${:.2f}".format(total)
