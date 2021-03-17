# Binary Search

Sequential Search is a method of comparing the item to the middle item of the list. Depending on this comparison(< or > or =), we repeat the process on the left or the right side of the list from the middle until the item is found(= case)


## Implementation(Python)

```python

#search method for ordered list 



def BinarySearch(l, item):
    if not l:
        return False
    midpoint = int(len(l)/2)
    #compare item to midpoint of the list repeat the process on the left or right from the middle side accordingly
    if item < l[midpoint]:
        #search on the left side  
        return BinarySearch(l[:midpoint],item)
    elif item > l[midpoint]:
        #search on the right side  
        return BinarySearch(l[midpoint+1:],item)
    else: 
        return True

  
```
Test on 2 cases: 

```python
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(BinarySearch(testlist, 3))
print(BinarySearch(testlist, 13))
```

Output:

```python
False
True
```


## Analysis

Time Complexity: O(logN)

However, python slicing list performs on O(n) so it might not perform regularly at O(logn)

```python
BinarySearch(l[:midpoint],item)
```

Alternatively, we can just change the index values instead of slicing the list

for example: 

```python
def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
	            last = midpoint-1
            else:
	            first = midpoint+1

    return found

#Source https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheBinarySearch.html
```

