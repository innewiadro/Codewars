def direction(facing, turn):
    directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    idx = directions.index(facing)
    steps = turn // 45
    return directions[(idx + steps) % 8]