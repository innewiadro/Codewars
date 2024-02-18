def people_with_age_drink(age):
    if age < 14:
        a = "drink toddy"
    elif 18 > age >= 14:
        a = "drink coke"
    elif 21 > age >= 18:
        a = "drink beer"
    elif age >= 21:
        a = "drink whisky"
    return a
