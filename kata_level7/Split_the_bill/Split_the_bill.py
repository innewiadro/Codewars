def split_the_bill(x):
    average = sum(x.values()) / len(x)
    result = {person: round(amount - average, 2) for person, amount in x.items()}

    return result
