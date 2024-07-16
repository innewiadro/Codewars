def find_screen_height(width, ratio):
    ratio_width, ratio_height = map(int, ratio.split(':'))
    height = width * ratio_height // ratio_width
    return f"{width}x{height}"
