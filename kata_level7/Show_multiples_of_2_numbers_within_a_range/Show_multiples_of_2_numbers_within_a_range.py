import math

def multiples(s1,s2,s3):
    lcm_ab = abs(s1 * s2) // math.gcd(s1, s2)
    return [i for i in range(lcm_ab, s3 , lcm_ab)]
