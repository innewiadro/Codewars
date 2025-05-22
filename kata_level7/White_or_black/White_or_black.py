def square_color(file, rank):
    col_number = ord(file.lower()) - ord('a') + 1
    return "black" if (col_number + rank) % 2 == 0 else "white"
