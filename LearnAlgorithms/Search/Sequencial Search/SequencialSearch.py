#Traverse through every single item in the list and return true if found an exact item. 

def SequentialSearch(l, data):
    found = False 
    for x in l:
        if x == data:
            found = True
    
    return found

testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(SequentialSearch(testlist, 3))
print(SequentialSearch(testlist, 13))