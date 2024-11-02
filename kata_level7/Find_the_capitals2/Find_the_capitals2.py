def capital(capitals):
    result = []
    for item in capitals:
        state = item.get('state')  or item.get('country')
        capital = item.get('capital')
        if state and capital:
            result.append(f"The capital of {state} is {capital}")
    return result
