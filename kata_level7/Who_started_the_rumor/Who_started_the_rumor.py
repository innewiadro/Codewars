def rumor_starter(record):
    senders = set(record.keys())
    receivers = set()

    for people in record.values():
        receivers.update(people)

    culprits = senders - receivers
    return sorted(culprits)
