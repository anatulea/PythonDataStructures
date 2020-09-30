def bubble_sort(arr):
    # For every element (arranged backwards)
    for n in range(len(arr)-1,0,-1):
        print(f'This is the n: {n}')
        for k in range(n):
            print(f'This is the k  index check: {k}')
            # If we come to a point to switch
            if arr[k]>arr[k+1]:
                temp = arr[k]
                arr[k] = arr[k+1]
                arr[k+1] = temp
            
arr = [3,2,13,4,6,5,7,8,1,20]
bubble_sort(arr)

print(arr)