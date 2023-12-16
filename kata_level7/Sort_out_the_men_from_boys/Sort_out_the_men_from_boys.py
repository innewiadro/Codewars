def men_from_boys(arr):
    our_set = set(arr)
    even_numbers = sorted([n for n in our_set if n % 2 == 0])
    odd_numbers = sorted([n for n in our_set if n % 2 != 0], reverse=True)
    return even_numbers + odd_numbers
