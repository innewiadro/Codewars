import math


def predict_age(*args):
    a = [i*i for i in args]
    return math.floor((sum(a)**0.5)/2)
