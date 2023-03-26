def find_next_square(sq):
    return ((sq**0.5)+1)**2 if round(sq**0.5) == sq**0.5 else -1
