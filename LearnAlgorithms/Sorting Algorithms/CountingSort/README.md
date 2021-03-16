# Counting Sort

Counting sort is a sorting technique based on keys between a specific range. It works by counting the number of objects having distinct key values (kind of hashing). Then doing some arithmetic to calculate the position of each object in the output sequenceInsertion sort is a sorting algorithm that sorts an array one item at a item by comparing to its adjacent item

Source: Geeksforgeeks

## Algorithm
 Rather than using a comparison, you create an integer array whose index range covers the entire range of values in your array to sort. Each time a value occurs in the original array, you increment the counter at that index. At the end, run through your counting array, printing the value of each non-zero valued index that number of times.

 Source: Hackerrank

## Example(Python)

```python

# Count each element's appearance( element ranging from 0 to 100 only)
def countingSort(arr):
    fre = [0]*100
    result = []
    for i in range(len(arr)):
        fre[arr[i]]+=1
    for k in range(len(fre)):
        if fre[k]> 0:
            for t in range(fre[k]):
                result.append(k)
    return result 
```

## Analysis

1. Counting sort is efficient if the range of input data is not significantly greater than the number of objects to be sorted. Consider the situation where the input sequence is between range 1 to 10K and the data is 10, 5, 10K, 5K. 

2. It is not a comparison based sorting. It running time complexity is O(n) with space proportional to the range of data. 

3. It is often used as a sub-routine to another sorting algorithm like radix sort. 

4. Counting sort uses a partial hashing to count the occurrence of the data object in O(1). 

5. Counting sort can be extended to work for negative inputs also.
