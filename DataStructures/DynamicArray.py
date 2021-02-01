import math 
queries = [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]
def dynamicArray(n, queries):
    arr = []
    for m in range(n):
        arr.append([])
    k = len(queries)
    la = 0 
    result = []
    for i in queries:
        if i[0] == 1:
            arr[((i[1])^la)%n].append(i[2])
        else:
            la =  arr[((i[1])^la)%n][i[2]]
            result.append(la)
            print(la)
    
    return result

print(dynamicArray(2,queries))



