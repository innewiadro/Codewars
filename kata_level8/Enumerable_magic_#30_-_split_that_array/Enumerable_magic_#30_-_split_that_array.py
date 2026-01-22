def partition(arr, classifier_method):
    new = []
    bad = []

    for i in arr:
        if classifier_method(i):
            new.append(i)
        else:
            bad.append(i)

    return new, bad
