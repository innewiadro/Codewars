def what_list_am_i_on(actions):
    naughty_letters = {'b', 'f', 'k'}
    nice_letters = {'g', 's', 'n'}

    naughty_count = 0
    nice_count = 0

    for action in actions:
        if not action:
            continue
        first_letter = action[0].lower()
        if first_letter in naughty_letters:
            naughty_count += 1
        elif first_letter in nice_letters:
            nice_count += 1

    return 'naughty' if naughty_count >= nice_count else 'nice'
