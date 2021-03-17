#Traverse through every single item in the list and return true if found an exact item. 

def SequentialSearch(data, l):
    found = False 
    for x in l:
        if x == data:
            found = True
    
    return found
