def total_licks(env):
    base = 252
    total = base + sum(env.values())

    toughest = None
    max_increase = 0
    for k, v in env.items():
        if v > max_increase:
            max_increase = v
            toughest = k

    if toughest:
        return f"It took {total} licks to get to the tootsie roll center of a tootsie pop. The toughest challenge was {toughest}."
    else:
        return f"It took {total} licks to get to the tootsie roll center of a tootsie pop."
