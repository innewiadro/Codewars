def count_squares(cuts):
    if cuts < 2:
        return (cuts + 1) ** 3
    return (cuts + 1) ** 3 - (cuts - 1) ** 3
