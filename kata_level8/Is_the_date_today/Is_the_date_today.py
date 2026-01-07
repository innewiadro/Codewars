from datetime import datetime

def is_today(given_date : datetime) -> bool:
    today = datetime.today()
    return (
        given_date.year == today.year and
        given_date.month == today.month and
        given_date.day == today.day
    )
