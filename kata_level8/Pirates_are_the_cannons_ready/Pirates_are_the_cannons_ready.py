def cannons_ready(gunners):
    for status in gunners.values():
        if status == 'nay':
            return 'Shiver me timbers!'
    return "Fire!"
