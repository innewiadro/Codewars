def calculate_age(year_of_birth, current_year):
    if abs(year_of_birth - current_year) == 1:
        year = "year"
    else:
        year = "years"
        
    if year_of_birth == current_year:
        return "You were born this very year!"
    elif year_of_birth > current_year:
        return f"You will be born in {year_of_birth - current_year} {year}."
    else:
        return f"You are {current_year - year_of_birth} {year} old."
