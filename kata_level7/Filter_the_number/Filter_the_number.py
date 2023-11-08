def filter_string(string):
    return int(''.join(filter(str.isdigit, string)))
