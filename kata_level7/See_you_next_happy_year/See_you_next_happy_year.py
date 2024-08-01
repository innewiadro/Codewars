def next_happy_year(year):
    def is_happy_year(y):
        return len(set(str(y))) == len(str(y))

    year += 1
    while not is_happy_year(year):
        year += 1
    return year
