def billboard(name, price=30):
    cost = 0
    for i in name:
        cost += price

    return cost
