import math 
def dynamicArray(n, queries):
    arr = []
    for m in range(n):
        arr.append([])
    print(arr)
    k = len(queries)
    la = 0 
    result = []
    for i in queries:
        if i[0] == 1:
            print(((i[1])^la)%n)
            arr[((i[1])^la)%n].append(i[2])
        else:
            print(((i[1])^la)%n)
            la =  arr[((i[1])^la)%n][i[2]% len(arr[((i[1])^la)%n])]
            result.append(la)
            print(la)
    
    return result

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

q = int(first_multiple_input[1])

queries = []

for _ in range(q):
    queries.append(list(map(int, input().rstrip().split())))
print(queries)
print(dynamicArray(n,queries))



