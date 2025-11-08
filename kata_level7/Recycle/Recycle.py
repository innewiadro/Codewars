def recycle_me(rubbish):
    plastic = sum(1 for x in rubbish if x > 0)
    glass = sum(1 for x in rubbish if x < 0)
    card = sum(1 for x in rubbish if x == 0)
    return plastic, glass, card
