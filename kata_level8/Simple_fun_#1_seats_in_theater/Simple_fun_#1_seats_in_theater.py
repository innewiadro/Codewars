def seats_in_theater(tot_cols, tot_rows, col, row):
    return (tot_rows - row) * (tot_cols - col + 1)
