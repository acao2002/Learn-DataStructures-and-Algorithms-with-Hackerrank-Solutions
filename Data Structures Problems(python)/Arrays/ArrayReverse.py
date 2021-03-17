a = [1,2,3,4]

def reverseArray(a):
    result = []
    for x in a:
        result.insert(-len(result),x)
    return result 

print(reverseArray(a))