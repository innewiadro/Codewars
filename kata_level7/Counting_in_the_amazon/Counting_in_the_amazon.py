def count_arara(n):
    adak_count = n // 2
    anane_count = n % 2
    return " ".join(["adak"] * adak_count + ["anane"] * anane_count)
