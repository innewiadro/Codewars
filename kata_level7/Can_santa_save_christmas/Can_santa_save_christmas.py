from datetime import datetime, timedelta


def determine_time(arr):
    time = timedelta()
    for i in arr:
        parsed_time = datetime.strptime(i, "%H:%M:%S")
        time += timedelta(hours=parsed_time.hour, minutes=parsed_time.minute, seconds=parsed_time.second)

    return time <= timedelta(hours=24)
