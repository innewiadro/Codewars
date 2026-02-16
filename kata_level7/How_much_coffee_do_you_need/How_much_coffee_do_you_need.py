def how_much_coffee(events):
    coffees = 0

    valid_events = {'cw', 'dog', 'cat', 'movie'}

    for event in events:
        if event.lower() in valid_events:
            if event.islower():
                coffees += 1
            elif event.isupper():
                coffees += 2

    if coffees > 3:
        return 'You need extra sleep'

    return coffees
