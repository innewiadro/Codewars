def rental_car_cost(d):
    total = d * 40
    if d > 6:
        total -= 50
    elif d > 3 or d < 6:
        total -= 20
    return total
