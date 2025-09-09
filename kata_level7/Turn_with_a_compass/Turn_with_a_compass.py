def direction(facing, turn):
    dirs = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    i = dirs.index(facing)
    steps = turn // 45
    return dirs[(i + steps) % 8]
