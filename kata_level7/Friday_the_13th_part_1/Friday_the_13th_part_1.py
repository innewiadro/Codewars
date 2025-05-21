def kill_count(counselors, jason):
    return [name for name, iq in counselors if iq < jason]
