import re


def remove_url_anchor(url):
    return re.sub(r'#.*', '', url)
