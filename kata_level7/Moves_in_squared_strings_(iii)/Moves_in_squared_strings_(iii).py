
def diag_1_sym(strng):
    rows = strng.split("\n")
    n = len(rows)

    return "\n".join(
        "".join(rows[row][col] for row in range(n))
        for col in range(n)
    )


def rot_90_clock(strng):
    rows = strng.split("\n")
    n = len(rows)

    return "\n".join(
        "".join(rows[row][col] for row in range(n - 1, -1, -1))
        for col in range(n)
    )


def selfie_and_diag1(strng):
    rows = strng.split("\n")
    diagonal = diag_1_sym(strng).split("\n")

    return "\n".join(
        original + "|" + transformed
        for original, transformed in zip(rows, diagonal)
    )


def oper(fct, strng):
    return fct(strng)