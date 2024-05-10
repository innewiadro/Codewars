def even_numbers(arr,n):
    return [el for el in arr if el % 2 == 0][-n:]
