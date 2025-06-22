def is_palindrome(n):
    return str(n) == str(n)[::-1]

def reverse_number(n):
    return int(str(n)[::-1])

def palindrome_chain_length(n):
    steps = 0
    while not is_palindrome(n):
        n += reverse_number(n)
        steps += 1
    return steps
