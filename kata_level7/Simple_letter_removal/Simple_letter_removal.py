def solve(st,k):
    for char in sorted(set(st)):  # Iterate through letters in alphabetical order
        while k > 0 and char in st:
            st = st.replace(char, '', 1)  # Remove leftmost occurrence of char
            k -= 1
    return st
