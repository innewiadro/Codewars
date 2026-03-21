import math


def tankvol(h, d, vt):
    r = d / 2

    segment_area = (
            r ** 2 * math.acos((r - h) / r)
            - (r - h) * math.sqrt(2 * r * h - h ** 2)
    )

    total_area = math.pi * r ** 2

    volume = (segment_area / total_area) * vt

    return int(volume)