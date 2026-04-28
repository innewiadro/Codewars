def wrapping_paper(boxes):
    total = 0

    for l, w, h in boxes:
        side1 = l * w
        side2 = w * h
        side3 = h * l

        surface_area = 2 * (side1 + side2 + side3)
        slack = min(side1, side2, side3)

        total += surface_area + slack

    return total