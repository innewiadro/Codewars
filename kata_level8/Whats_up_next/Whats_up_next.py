def next_item(sequence, item):
    iterator = iter(sequence)
    for current_item in iterator:
        if current_item == item:
            return next(iterator, None)
