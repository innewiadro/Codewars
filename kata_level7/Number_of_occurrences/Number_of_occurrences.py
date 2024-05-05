def number_of_occurrences(element, sample):
    counter = 0
    for i in sample:
        if i == element:
            counter += 1
    return counter
