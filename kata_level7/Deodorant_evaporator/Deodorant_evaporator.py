def evaporator(content, evap_per_day, threshold):
    count = 0
    limit = threshold * content * 0.01
    while content >= limit:
        content -= content * 0.01 * evap_per_day
        count += 1
    return count
