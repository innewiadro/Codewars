def get_rectangle_string(width, height):
    top = "*" * width + "\r\n"

    if height > 2:
        middle = "*" + " " * (width - 2) + "*\r\n"
        middle_rows = middle * (height - 2)
    else:
        middle_rows = ""

    bottom = "*" * width + "\r\n" if height > 1 else ""

    return top + middle_rows + bottom
