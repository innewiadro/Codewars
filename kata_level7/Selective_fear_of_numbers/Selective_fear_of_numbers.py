def am_I_afraid(day, num):
    scary_numbers = {
        'Monday': lambda n: n == 12,
        'Tuesday': lambda n: n > 95,
        'Wednesday': lambda n: n == 34,
        'Thursday': lambda n: n == 0,
        'Friday': lambda n: n % 2 == 0,
        'Saturday': lambda n: n == 56,
        'Sunday': lambda n: n in (666, -666),
    }

    return scary_numbers[day](num)
