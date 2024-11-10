def search_names(logins):
    return list(filter(lambda pair: pair[0].endswith('_'), logins))
