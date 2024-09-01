def killer(suspects, dead):
    for suspect, seen_people in suspects.items():
        if all(person in seen_people for person in dead):
            return suspect
    return None
