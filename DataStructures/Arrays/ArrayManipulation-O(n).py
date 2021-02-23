

def arrayManipulation(n, queries):
    array = [0]*(n + 1)
    for x in queries:
        array[x[0]-1] += x[2]
        array[x[1]] -= x[2]

    maxs = 0
    sums = 0
    for y in array:
        sums += y
        maxs = max(maxs,sums)
    return maxs

nm = input().split()

n = int(nm[0])

m = int(nm[1])

queries = []

for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

result = arrayManipulation(n, queries)
print(result)