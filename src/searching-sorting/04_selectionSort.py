'''
The selection sort improves on the bubble sort by making only one exchange for every pass through the list. In order to do this, a selection sort looks for the largest value as it makes a pass and, after completing the pass, places it in the proper location. As with a bubble sort, after the first pass, the largest item is in the correct place. After the second pass, the next largest is in place. This process continues and requires n−1 passes to sort n items, since the final item must be in place after the (n−1) st pass.
'''
def selectionSort(arr):
    for slot in range(len(arr)-1, 0, -1):
        print(f'Slot:{slot}')
        maxPosition = 0
        for location in range(1, slot+1):
            print(f'Location: {location}')
            if arr[location] > arr[maxPosition]:
                maxPosition = location
        temp = arr[slot]
        arr[slot] = arr[maxPosition]
        arr[maxPosition]= temp
    return arr

mylist = [1,4,2,8,3,7,3,5,33]

print(selectionSort(mylist))
