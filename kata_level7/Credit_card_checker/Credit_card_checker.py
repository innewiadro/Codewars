def valid_card(card):
    digits = card.replace(" ", "")
    digits = [int(d) for d in digits]
    total = 0
    reversed_digits = digits[::-1]

    for i, digit in enumerate(reversed_digits):
        if i % 2 == 1:
            doubled = digit * 2
            if doubled > 9:
                doubled -= 9
            total += doubled
        else:
            total += digit

    return total % 10 == 0
