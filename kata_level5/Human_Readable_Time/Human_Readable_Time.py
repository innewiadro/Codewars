def make_readable(seconds):
    mins = seconds // 60
    seconds %= 60
    hours = mins // 60
    mins %= 60

    if len(str(hours)) == 1:
        hours = "0" + str(hours)

    if len(str(mins)) == 1:
        mins = "0" + str(mins)
    if len(str(seconds)) == 1:
        seconds = "0" + str(seconds)
        
    return f'{hours}:{mins}:{seconds}'
