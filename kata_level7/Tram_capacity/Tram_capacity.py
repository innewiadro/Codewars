def tram(stops, descending, onboarding):
    current = 0
    max_capacity = 0

    for i in range(stops):
        current -= descending[i]
        current += onboarding[i]
        max_capacity = max(max_capacity, current)

    return max_capacity
