def list_to_array(linked_list):
    result = []
    current = linked_list
    while current:
        result.append(current.value)
        current = current.next
    return result
