def binary_search(arr, val):
    left_pointer = 0
    right_pointer = len(arr) - 1
    found = False

    while left_pointer <= right_pointer and not found:
        mid = (left_pointer+right_pointer)//2

        if arr[mid] == val:
            found = True
        else:
            if mid > val:
                right_pointer = mid - 1
            elif mid < val:
                left_pointer = mid + 1
    return found


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8], 9))
