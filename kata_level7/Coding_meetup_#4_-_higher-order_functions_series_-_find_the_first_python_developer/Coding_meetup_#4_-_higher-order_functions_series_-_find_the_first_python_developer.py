def get_first_python(users):
    users = next((person for person in users if person["language"] == "Python"), None)

    return f"{users['first_name']}, {users['country']}" if users else "There will be no Python developers"
