def format_duration(seconds):
    if not seconds:
        return "now"
    else:
        mins = seconds // 60
        seconds %= 60
        hours = mins // 60
        mins %= 60
        days = hours // 24
        hours %= 24
        years = days // 365
        days %= 365

        time_list = [years, days, hours, mins, seconds]
        
        time = ["year", "day", "hour", "minute", "second"]

        result_list = []           
        
        for i in range(len(time_list)):
            if time_list[i] != 0:
                if time_list[i] > 1:
                    result_list.append(str(time_list[i]) + " " + time[i] + 's')
                else:
                    result_list.append(str(time_list[i]) + " " + time[i])

        if len(result_list) == 1:
            return result_list[0]
        elif len(result_list) == 2:
            return result_list[0] + " and " + result_list[1]
        else:
            return ', '.join(result_list[:-1]) + " and " + result_list[-1]
