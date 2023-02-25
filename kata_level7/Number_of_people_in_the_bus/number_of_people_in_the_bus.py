def number(bus_stops):
    ppl_in_bus = 0

    for i in bus_stops:
        ppl_in_bus += i[0] - i[1]
    return ppl_in_bus
