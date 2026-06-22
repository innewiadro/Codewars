def get_average(lst):
    total_age = sum(dev['age'] for dev in lst)
    average = total_age / len(lst)
    return round(average)
