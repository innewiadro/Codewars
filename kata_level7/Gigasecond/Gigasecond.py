from datetime import datetime, timedelta


def gigasecond(start_date):
    dt = datetime.combine(start_date, datetime.min.time())

    gigasecond = timedelta(seconds=10**9)
    result = dt + gigasecond

    return result.date()
