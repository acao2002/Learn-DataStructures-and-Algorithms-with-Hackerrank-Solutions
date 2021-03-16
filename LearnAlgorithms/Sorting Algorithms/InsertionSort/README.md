# Insertion Sort

Insertion sort is a sorting algorithm that sorts an array one item at a item by comparing to its adjacent item

## Algorithm

To sort an array of size n in ascending order: 

1: Iterate from arr[1] to arr[n] over the array. 

2: Compare the current element (key) to its predecessor. 

3: If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.

source: geeksforgeeks


## Example(Python)


```python

def insertion_sort(l):
    for i in range(1, len(l)):
        key = l[i]
        while i>0 and key<l[i-1]:
            l[i]=l[i-1] #shift element to the right if < key 
            i=i-1
        l[i] = key #insert key at the end of loop
```

## Time complexity 

O(N) for simple cases and O(N^2) for complicated cases 
=> useful for simple, nearly sorted arrays but not efficient for completely unsorted big arrays

