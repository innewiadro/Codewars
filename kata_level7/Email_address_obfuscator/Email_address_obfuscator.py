def obfuscate_email(email):
    return email.replace('.', ' [dot] ').replace('@', ' [at] ')
