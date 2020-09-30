def seq_search(arr, ele):
    pos = 0
    found = False
    while pos < len(arr) and not found:
        if arr[pos]==ele:
            found = True
        else:
            pos += 1
    return found

arr = [1,2,3,4,5]
print(seq_search(arr, 3))
print(seq_search(arr, 8))

def ordered_seq_search(arr, ele):
    # input must be sorted/ ordered 
    pos = 0
    found = False
    stopped = False
    while pos < len(arr) and not found and not stopped:
        if arr[pos] == ele:
            found = True
        else:
            if arr[pos]>ele:
                stopped = True
            else:
                pos += 1
    return found

arr = [1,2,3,4,5]
print(ordered_seq_search(arr, 3))
print(ordered_seq_search(arr, 8))