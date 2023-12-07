def sum_triangular_numbers(n):
    sum_of_tri = 0
    for i in range(1, n+1):
        sum_of_tri += i*(i+1)/2
    return sum_of_tri
