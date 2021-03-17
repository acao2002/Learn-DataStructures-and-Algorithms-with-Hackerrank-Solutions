# Sequential Search

Sequential Search is a method of going through every item in a list linearly until finding the desirable item. 


## Implementation(Python)

```python

#Traverse through every single item in the list and return true if found an exact item. 

def SequentialSearch(data, l):
    found = False 
    for x in l:
        if x == data:
            found = True
    
    return found

  
```

## Analysis

Time Complexity: O(N)

When using Sequential Search for ordered lists, you can set a stop signal whenever the item in the list is larger than the desired item to improve the performance. 

