def remove(s):
    parts = s.split('!')
    result = ''.join(parts[:-1]) + '!' * len(parts[-1])
    return result if result.endswith('!') else result.rstrip('!')
