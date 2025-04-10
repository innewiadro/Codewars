def list_animals(animals):
    result = ""
    for i, animal in enumerate(animals, 1):
        result += f"{i}. {animal}\n"
    return result
