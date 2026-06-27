def gimme_the_letters(sp):
    start, end = sp.split("-")
    return "".join(chr(i) for i in range(ord(start), ord(end) + 1))