def solution(M1, M2, m1, m2, V, T):
    R = 0.082
    T_kelvin = T + 273.15

    n1 = m1 / M1
    n2 = m2 / M2

    P_total = ((n1 + n2) * R * T_kelvin) / V
    return P_total
