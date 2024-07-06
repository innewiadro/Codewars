def time_correct(t):

    if t == "":
        return ""
    try:
        hours, minutes, seconds = map(int, t.split(':'))
    except:
        return None

    if len(t) > 8:
        return None

    add_min, corrected_seconds = divmod(seconds, 60)

    total_minutes = hours * 60 + minutes + add_min

    corrected_hours, corrected_minutes = divmod(total_minutes, 60)

    _, corrected_hours = divmod(corrected_hours, 24)

    return f"{corrected_hours:02}:{corrected_minutes:02}:{corrected_seconds:02}"