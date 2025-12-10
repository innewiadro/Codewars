def pick(preferred, blacklisted, options):
    labels = ["A", "B", "C"]
    preferred_opts = []
    neutral_opts = []

    for label, (skill, pct) in zip(labels, options):
        if skill in blacklisted:
            continue
        if skill in preferred:
            preferred_opts.append((pct, label))
        else:
            neutral_opts.append((pct, label))

    if preferred_opts:
        return max(preferred_opts)[1]

    if neutral_opts:
        return max(neutral_opts)[1]

    return "D"
