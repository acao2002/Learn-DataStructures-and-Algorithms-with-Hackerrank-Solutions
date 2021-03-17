def BinarySearch(l, item):
    if not l:
        return False
    midpoint = int(len(l)/2)
    if item < l[midpoint]:
        return BinarySearch(l[:midpoint],item)
    elif item > l[midpoint]:
        return BinarySearch(l[midpoint+1:],item)
    else: 
        return True


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(BinarySearch(testlist, 3))
print(BinarySearch(testlist, 13))
