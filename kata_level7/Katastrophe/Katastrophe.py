import math


def strong_enough(earthquake, age):
    earth_sum = []
    for i in earthquake:
        earth_sum.append(sum(i))

    res = math.prod(earth_sum)

    strength = 1000
    strength = strength * math.exp(-0.01 * age)
    return "Safe!" if strength >= res else "Needs Reinforcement!"
