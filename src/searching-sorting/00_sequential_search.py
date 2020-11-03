def seq_search(arr, target):
    pos = 0
    found = False
    while pos < len(arr) and not found:
        if arr[pos]==target:
            found = True
        else:
            pos += 1
    return found

arr = [1,2,3,4,5]
print(seq_search(arr, 3))
print(seq_search(arr, 8))


# If we know the list is ordered than, we only have to check until we have found the element or an element greater than it.
def ordered_seq_search(arr, target):
    # input must be sorted/ ordered 
    pos = 0
    found = False
    stopped = False
    while pos < len(arr) and not found and not stopped:
        if arr[pos] == target:
            found = True
        else:
            if arr[pos]>target:
                stopped = True
            else:
                pos += 1
    return found

arr = [1,2,3,4,5]
print(ordered_seq_search(arr, 3))
print(ordered_seq_search(arr, 8))