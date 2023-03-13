def divisors(integer):
    list_of_div = [i for i in range(2,integer) if integer % i == 0]
    return list_of_div if len(list_of_div) != 0 else f'{integer} is prime'
