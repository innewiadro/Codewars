def driver(data):
    first_name = data[0]
    middle_name = data[1]
    surname = data[2].upper()
    dob = data[3]
    gender = data[4].upper()
    surname_code = (surname[:5] + "99999")[:5]
    day, month, year = dob.split('-')

    month_map = {
        "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
        "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
        "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
    }

    month = month_map[month[:3]] if month[:3] in month_map else month.zfill(2)
    decade_digit = year[2]
    year_digit = year[3]
    month_code = int(month) + (50 if gender == 'F' else 0)
    month_code = str(month_code).zfill(2)
    day_code = day.zfill(2)
    initials = first_name[0] + (middle_name[0] if middle_name else "9")
    arbitrary_digit = "9"
    check_digits = "AA"
    license_number = f"{surname_code}{decade_digit}{month_code}{day_code}{year_digit}{initials}{arbitrary_digit}{check_digits}"

    return license_number
