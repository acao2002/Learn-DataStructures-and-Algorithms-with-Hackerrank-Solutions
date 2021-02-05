def arrayManipulation(n, queries):
    array = [0]*n
    for x in queries:
        for i in range(x[0]-1, x[1]):
            array[i]+= x[2]
    return max(array)