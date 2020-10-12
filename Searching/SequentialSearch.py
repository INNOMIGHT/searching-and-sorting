def seq_search(arr, val):
    counter = 0
    found = False

    while not found:
        if arr[counter] == val:
            found = True
        else:
            counter += 1
    return found


print(seq_search([1, 2, 3, 4, 5], 2))
