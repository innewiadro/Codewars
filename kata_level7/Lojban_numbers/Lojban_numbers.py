def convert_lojban(lojban):
    lojban_digits = {
        'no': '0', 'pa': '1', 're': '2', 'ci': '3', 'vo': '4',
        'mu': '5', 'xa': '6', 'ze': '7', 'bi': '8', 'so': '9'
    }

    result = ''
    i = 0
    while i < len(lojban):
        part = lojban[i:i + 2]
        if part in lojban_digits:
            result += lojban_digits[part]
            i += 2
        else:
            raise ValueError(f"Invalid Lojban digit: {part}")

    return int(result)
