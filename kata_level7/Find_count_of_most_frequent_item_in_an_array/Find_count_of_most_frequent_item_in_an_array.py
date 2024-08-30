def most_frequent_item_count(collection):
    if not collection:
        return 0

    frequency = {}

    for item in collection:

        if item in frequency:

            frequency[item] += 1

        else:

            frequency[item] = 1

    max_count = max(frequency.values())

    return max_count
