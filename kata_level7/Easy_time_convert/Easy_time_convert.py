def time_convert(num):
    if num <= 0:
        return "00:00"

    hours = num // 60
    mins = num % 60

    return f"{hours:02}:{mins:02}"
