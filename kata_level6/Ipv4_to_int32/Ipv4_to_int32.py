def ip_to_int32(ip):
    octets = map(int, ip.split('.'))

    result = 0
    for octet in octets:
        result = (result << 8) | octet
    return result
