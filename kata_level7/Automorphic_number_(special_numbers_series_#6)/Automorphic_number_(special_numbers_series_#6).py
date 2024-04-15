def automorphic(n):
    return "Automorphic" if str(n ** 2)[-len(str(n))::] == str(n) else "Not!!"
