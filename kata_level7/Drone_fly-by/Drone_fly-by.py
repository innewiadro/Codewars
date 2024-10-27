def fly_by(lamps, drone):
    flight_length = len(drone)
    return 'o' * min(flight_length, len(lamps)) + lamps[flight_length:]
