

def arrayManipulation(n, queries):
    array = [0]*n
    for x in queries:
        for i in range(x[0]-1, x[1]):
            array[i]+= x[2]
    return max(array)

nm = input().split()

n = int(nm[0])

m = int(nm[1])

queries = []

for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

result = arrayManipulation(n, queries)
