def pyramid(balls):
    level = 0
    total = 0
    while total + level < balls:
        level += 1
        total += level
    return level
