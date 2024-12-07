def solve(a):
    even_count = 0
    odd_count = 0

    for item in a:

        if isinstance(item, int) or (isinstance(item, str) and item.isdigit()):

            num = int(item)
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    return even_count - odd_count