def get_grade(s1, s2, s3):
    avg = (s1 + s2 + s3) / 3
    if avg >= 90:
        val = "A"
    elif avg >= 80:
        val = "B"
    elif avg >= 70:
        val = "C"
    elif avg >= 60:
        val = "D"
    else:
        val = 'F'
    return val
