def cog_RPM(cogs):
    rpm = 1.0
    direction = 1

    for i in range(len(cogs) - 1):
        rpm *= cogs[i] / cogs[i + 1]
        direction *= -1

    return direction * rpm
