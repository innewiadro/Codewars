from datetime import date, timedelta


def unlucky_days(year):
    res = 0

    start = date(year, 1, 1)
    end = date(year, 12, 31)
    day = timedelta(days=1)

    while start <= end:

        if start.strftime("%A %d") == "Friday 13":
            res += 1

        start += day

    return res
