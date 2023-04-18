def speed_limit(speed, signals):
    fine = 0
    for i in signals:
        if i < speed:
            if speed >= i + 30:
                fine += 500
            elif speed >= i + 20:
                fine += 250
            elif speed >= i + 10:
                fine += 100
    return fine
