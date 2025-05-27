from preloaded import animals, elements


def chinese_zodiac(year):

    base_year = 1984
    diff = year - base_year

    animal = animals[diff % 12]
    element = elements[(diff // 2) % 5]

    return f"{element} {animal}"