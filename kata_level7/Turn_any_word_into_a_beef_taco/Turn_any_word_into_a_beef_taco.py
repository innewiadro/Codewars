def tacofy(word):
    ingredient_map = {
        **dict.fromkeys("aeiou", "beef"),
        "t": "tomato",
        "l": "lettuce",
        "c": "cheese",
        "g": "guacamole",
        "s": "salsa"
    }

    taco = ["shell"]

    for char in word.lower():
        if char in ingredient_map:
            taco.append(ingredient_map[char])

    return taco + ["shell"]
