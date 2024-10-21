import math

numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
           "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]

def wallpaper(l, w, h):
    if l == 0 or w == 0 or h == 0:
        return numbers[0]

    total_area = 2 * (l * h + w * h)

    required_area = total_area * 1.15

    roll_coverage = 5.2

    num_rolls = math.ceil(required_area / roll_coverage)

    return numbers[num_rolls]