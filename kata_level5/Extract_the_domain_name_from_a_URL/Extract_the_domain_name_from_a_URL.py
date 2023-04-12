def domain_name(url):
    a = [i for i in url.split("/")]
    for item in a:
        if '.' in item:
            b = item.split(".")
            if b[0] == 'www':
                return b[1]
            else:
                return b[0]
