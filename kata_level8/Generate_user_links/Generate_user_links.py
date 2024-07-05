import urllib.parse


def generate_link(user):
    text = urllib.parse.quote(user)
    return f'http://www.codewars.com/users/{text}'
