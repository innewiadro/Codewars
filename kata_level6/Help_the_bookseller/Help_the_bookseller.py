def stock_list(list_of_art, list_of_cat):
    if not list_of_art or not list_of_cat:
        return ""

    counts = {c: 0 for c in list_of_cat}

    for art in list_of_art:
        code, qty = art.split()
        cat = code[0]
        if cat in counts:
            counts[cat] += int(qty)

    return " - ".join(f"({c} : {counts[c]})" for c in list_of_cat)
