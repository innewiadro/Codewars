def battle(x, y):
    power_x = sum(ord(char) - ord('A') + 1 for char in x)
    power_y = sum(ord(char) - ord('A') + 1 for char in y)

    if power_x > power_y:
        return x
    elif power_y > power_x:
        return y
    else:
        return "Tie!"