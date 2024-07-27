def gps(s, x):
    if len(x) <= 1:
        return 0

    hourly_speed_list = []
    for i in range(len(x)-1):
        delta_distance = abs(x[i] - x[i+1])
        hourly_speed = 3600 * delta_distance / s
        hourly_speed_list.append(hourly_speed)

    return max(hourly_speed_list)
