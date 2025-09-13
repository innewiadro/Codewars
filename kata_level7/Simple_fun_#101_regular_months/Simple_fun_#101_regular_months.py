import datetime


def regular_months(curr_month):
    month, year = map(int, curr_month.split("-"))
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1

    while True:
        if datetime.date(year, month, 1).weekday() == 0:
            return f"{month:02d}-{year}"

        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
