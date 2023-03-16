def format_duration(seconds):
    if not seconds:
        return "now"
    else:
        minute = 60
        hour = 3600
        day = 3600 * 24
        year = 3600 * 24 * 365

        date_year = seconds // year

        day_s = seconds % year
        
        date_day = day_s // day

        hours_s = day_s % day  

        date_hour = hours_s // hour
        
        min_s = hours_s % hour

        date_min = min_s // minute
        
        date_sec = min_s % 60

        time = ["year", "day", "hour", "minute", "second"]
        times = ["years", "days", "hours", "minutes", "seconds"]

        if date_year == 0:
            string_year = ""
        elif date_year == 1:
            string_year = str(date_year) + " " + time[0]
        else:
            string_year = str(date_year) + " " + times[0]

        if date_day == 0:
            string_day = ""
        elif date_day == 1:
            string_day = str(date_day) + " " + time[1]
        else:
            string_day = str(date_day) + " " + times[1]

        if date_hour == 0:
            string_hour = ""
        elif date_hour == 1:
            string_hour = str(date_hour) + " " + time[2]
        else:
            string_hour = str(date_hour) + " " + times[2]

        if date_min == 0:
            string_min = ""
        elif date_min == 1:
            string_min = str(date_min) + " " + time[3]
        else:
            string_min = str(date_min) + " " + times[3]

        if date_sec == 0:
            string_sec = ""
        elif date_sec == 1:
            string_sec = str(date_sec) + " " + time[4]
        else:
            string_sec = str(date_sec) + " " + times[4]

        if date_day > 0 and date_year > 0:
            string_year = string_year + ", "

        if date_hour > 0 and date_day > 0:
            string_day = string_day + ", " 
        elif date_hour <= 0 and date_day > 0:
            string_day = string_day + ", " 

        if date_min > 0 and date_hour > 0 and date_sec <= 0:
            string_hour = string_hour + " and "
        elif date_min > 0 and date_hour > 0:
            string_hour = string_hour + ", "
        elif date_min > 0 and date_hour > 0:
            string_hour = string_hour + ", "

        if (date_year > 0 or date_day > 0 or date_hour > 0 or date_min > 0) and date_sec > 0:
            string_sec = " and " + string_sec
            
        return f'{string_year}{string_day}{string_hour}{string_min}{string_sec}'
