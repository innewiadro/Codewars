def alias_gen(f_name, l_name):
    if f_name[0].upper() in FIRST_NAME and l_name[0].upper() in SURNAME:
        return f'{FIRST_NAME[f_name[0].upper()]} {SURNAME[l_name[0].upper()]}'
    else:
        return 'Your name must start with a letter from A - Z.'
