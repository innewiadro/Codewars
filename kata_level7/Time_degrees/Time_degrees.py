def clock_degree(s) :
    if not isinstance(s, str):
        return "Check your time !"

    if len(s) != 5 or s[2] != ":":
        return "Check your time !"

    hh, mm = s.split(":")

    if not (hh.isdigit() and mm.isdigit()):
        return "Check your time !"

    hour = int(hh)
    minute = int(mm)
    if s == "24:00":
        return "Check your time !"


    if not (0 <= hour <= 23) or not (0 <= minute <= 59):
        return "Check your time !"


    snapped_hour = hour % 12
    hour_deg = snapped_hour * 30
    minute_deg = minute * 6

    if hour_deg == 0:
        hour_deg = 360

    if minute_deg == 0:
        minute_deg = 360

    return f"{hour_deg}:{minute_deg}"
