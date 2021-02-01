import math 
queries = [1, 0, 5,
1, 1, 7,
1, 0, 3,
2, 1, 0,
2, 1, 1]
def dynamicArray(n, queries):
    arr =[n][0]
    k = len(queries)
    la = 0 
    result = []
    for i in range(0,k,3):
        if queries[i] == 1:
            arr[((i+1)^la)%n].append(i+2)
            print('la 1')
        elif i == 2:
            la = arr[((i+1)^la)%n][i+2]
            result.append(la)
            print(la)
    
    return result

dynamicArray(2,queries)



