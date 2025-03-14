def change(st):
    s = st.lower()
    return ''.join('1' if chr(i) in s else '0' for i in range(97, 123))
