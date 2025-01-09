def modify_multiply(st, loc, num):
    words = st.split()
    word = words[loc]
    return '-'.join([word] * num)
