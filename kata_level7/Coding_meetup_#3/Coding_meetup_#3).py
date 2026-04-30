def is_ruby_coming(lst):
    return any(dev['language'] == 'Ruby' for dev in lst)