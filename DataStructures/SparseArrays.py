def matchingStrings(strings, queries):
    result =[]
    count = 0 
    for x in queries:
        for y in strings:
            if x == y:
                count +=1
        result.append(count)
        count = 0; 
    return result 
