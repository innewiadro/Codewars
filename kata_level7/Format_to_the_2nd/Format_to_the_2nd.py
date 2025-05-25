def print_nums(*args):
    if not args:
        return ""
    max_width = len(str(max(args)))
    formatted = [str(num).zfill(max_width) for num in args]
    return '\n'.join(formatted)
