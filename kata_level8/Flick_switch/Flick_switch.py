def flick_switch(lst):
    run = True
    bool_list = []

    for item in lst:
        if item == 'flick' and run:
            run = False
        elif item == 'flick' and not run:
            run = True

        bool_list.append(run)

    return bool_list
