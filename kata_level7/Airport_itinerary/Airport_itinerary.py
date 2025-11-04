def itinerary(trips):
    print(trips)
    route = []

    for trip in trips:
        if not route:
            route.append(trip['in'])
            route.append(trip['out'])
        else:
            if trip['in'] == route[-1]:
                route.append(trip['out'])
            else:
                route.append(trip['in'])
                route.append(trip['out'])

    return '-'.join(route)
