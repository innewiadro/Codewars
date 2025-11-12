def find_employees_role(name):
    parts = name.split()
    if len(parts) != 2:
        return "Does not work here!"

    first_name, last_name = parts
    for emp in employees:
        if emp['first_name'] == first_name and emp['last_name'] == last_name:
            return emp['role']
    return "Does not work here!"
