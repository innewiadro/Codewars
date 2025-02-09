def cake(candles, debris):
    if candles == 0:
        return "That was close!"

    fd = sum(
        ord(char) if i % 2 == 0 else ord(char) - 96
        for i, char in enumerate(debris)
    )

    return "Fire!" if fd > 0.7 * candles else "That was close!"
