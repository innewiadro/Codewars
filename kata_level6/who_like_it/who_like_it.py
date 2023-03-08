def likes(names):
    if len(names) == 0:
        string = "no one likes this"
    elif len(names) ==1:
        string = f'{names[0]} likes this'
    elif len(names) == 2:
        string = f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
        string = f'{names[0]}, {names[1]} and {names[2]} like this'
    else:
        string = f'{names[0]}, {names[1]} and {len(names)-2} others like this'

    return string
