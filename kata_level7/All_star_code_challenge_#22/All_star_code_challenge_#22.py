def to_time(seconds):
    h = seconds//3600
    m = seconds - h * 3600
    return f'{h} hour(s) and {m//60} minute(s)'
