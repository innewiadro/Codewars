def task(w, n, c):
    workers = {
        "Monday": "James",
        "Tuesday": "John",
        "Wednesday": "Robert",
        "Thursday": "Michael",
        "Friday": "William"
    }

    if w not in workers:
        return "Invalid weekday. Workers only work from Monday to Friday."

    worker = workers[w]
    total_cost = n * c

    return (f"It is {w} today, {worker}, you have to work, you must spray {n} trees "
            f"and you need {total_cost} dollars to buy liquid")
