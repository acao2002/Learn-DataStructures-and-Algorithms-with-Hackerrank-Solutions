

# Count each element's appearance(range 0 to 100) 
def countingSort(arr):
    fre = [0]*100
    result = []
    for i in range(len(arr)):
        fre[arr[i]]+=1
    for k in range(len(fre)):
        if fre[k]> 0:
            for t in range(fre[k]):
                result.append(k)
    return result 