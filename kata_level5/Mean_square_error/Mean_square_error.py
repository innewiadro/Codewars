def solution(array_a, array_b):
    mes = []

    for i in range(len(array_a)):
        mes.append((array_a[i] - array_b[i]) ** 2)

    return sum(mes) / len(array_a)
