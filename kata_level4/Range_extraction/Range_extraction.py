from itertools import groupby


def solution(args):
    output = []
    string = ""
    for i, j in groupby(enumerate(args), lambda x: x[0] - x[1]):
        output.append([z for i, z in j])

    for q in output:
        if len(q) == 1:
            string += str(q[0]) + ","

        elif len(q) == 2:
            string += str(q[0]) + "," + str(q[1]) + ","

        else:
            string += str(q[0]) + '-' + str(q[len(q) - 1]) + ","

    return string[:-1]
