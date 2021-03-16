#partition array into left, equal, and right sub arrays

def quickSort(arr):
    left = []
    right = []
    equal = []
    pivot = arr[0]
    equal.append(pivot)
    
    for i in range(1, len(arr)):
        if arr[i] > pivot:
            right.append(arr[i])
        elif arr[i] < pivot: 
            left.append(arr[i])
        else:
            equal.append(arr[i])
            
    return left+equal+right