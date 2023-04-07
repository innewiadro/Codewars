def find_needle(haystack):
    count = 0
    for i in haystack:
        if i == 'needle':
            return f'found the needle at position {count}'
        count += 1
