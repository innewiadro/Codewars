def is_flush(cards):
    colors = set()
    for i in cards:
        colors.add(i[-1])
    return False if len(colors) > 1 else True
