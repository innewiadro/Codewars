def warn_the_sheep(queue):
    position = len(queue) - 1 - queue.index("wolf")
    if position == 0:
        return "Pls go away and stop eating my sheep"
    else:
        return f"Oi! Sheep number {position}! You are about to be eaten by a wolf!"
