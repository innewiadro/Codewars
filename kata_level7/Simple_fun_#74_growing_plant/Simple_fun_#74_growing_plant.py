import math


def growing_plant(up_speed, down_speed, desired_height):
    if desired_height <= up_speed:
        return 1

    net_growth = up_speed - down_speed
    remaining_height = desired_height - up_speed

    days_before_last = math.ceil(remaining_height / net_growth)

    return days_before_last + 1
