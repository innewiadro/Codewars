def triangle(row):
    while len(row) > 1:
        new_row = ""
        for i in range(len(row) - 1):
            a, b = row[i], row[i + 1]

            if a == b:
                new_row += a
            else:
                colors = {"R", "G", "B"}
                new_row += (colors - {a, b}).pop()

        row = new_row

    return row
