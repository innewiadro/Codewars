def find_spaceship(astromap):
    rows = astromap.split('\n')
    for y, row in enumerate(reversed(rows)):
        x = row.find('X')
        if x != -1:
            return [x, y]
    return "Spaceship lost forever."
