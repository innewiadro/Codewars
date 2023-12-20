import math


def calculate_tip(amount, rating):
    tip_meter = {"terrible": 0,
                 "poor": 0.05,
                 "good": 0.10,
                 "great": 0.15,
                 "excellent": 0.20}
    return math.ceil(amount * tip_meter[rating.lower()]) if rating.lower() in tip_meter else 'Rating not recognised'
