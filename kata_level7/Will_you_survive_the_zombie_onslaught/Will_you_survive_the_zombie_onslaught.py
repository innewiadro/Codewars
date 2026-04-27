def zombie_shootout(zombies, distance, ammo):
    print(zombies, distance, ammo)
    time_limit = int(distance * 2)
    kills = min(zombies, ammo, time_limit)

    if kills == zombies:
        return f"You shot all {zombies} zombies."

    if ammo < zombies and ammo < time_limit:
        return f"You shot {kills} zombies before being eaten: ran out of ammo."

    return f"You shot {kills} zombies before being eaten: overwhelmed."
