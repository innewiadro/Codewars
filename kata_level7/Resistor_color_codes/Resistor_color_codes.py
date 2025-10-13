def decode_resistor_colors(bands):
    color_values = {
        "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
        "green": 5, "blue": 6, "violet": 7, "gray": 8, "white": 9
    }

    tolerance_values = {
        "gold": 5, "silver": 10
    }

    parts = bands.split()

    first_digit = color_values[parts[0]]
    second_digit = color_values[parts[1]]
    multiplier = color_values[parts[2]]

    ohms = (first_digit * 10 + second_digit) * (10 ** multiplier)

    if len(parts) == 4:
        tolerance = tolerance_values.get(parts[3], 20)
    else:
        tolerance = 20

    if ohms >= 1_000_000:
        value = f"{ohms / 1_000_000:g}M"
    elif ohms >= 1_000:
        value = f"{ohms / 1_000:g}k"
    else:
        value = str(int(ohms))

    return f"{value} ohms, {tolerance}%"
