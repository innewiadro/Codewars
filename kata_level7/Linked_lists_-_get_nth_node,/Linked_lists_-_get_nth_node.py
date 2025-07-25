def get_nth(node, index):
    current = node
    count = 0

    while current:
        if count == index:
            return current
        current = current.next
        count += 1
