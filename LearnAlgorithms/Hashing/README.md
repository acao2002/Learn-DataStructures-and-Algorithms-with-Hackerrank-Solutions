# Hashing

A hash table is a collection of items which are stored in such a way as to make it easy to find them later. Each position of the hash table, often called a slot, can hold an item and is named by an integer value starting at 0. For example, we will have a slot named 0, a slot named 1, a slot named 2, and so on. 

# Hash function

The mapping between an item and the slot where that item belongs in the hash table is called the hash function. 


Given a collection of items, a hash function that maps each item into a unique slot is referred to as a perfect hash function. If we know the items and the collection will never change, then it is possible to construct a perfect hash function (refer to the exercises for more about perfect hash functions). Unfortunately, given an arbitrary collection of items, there is no systematic way to construct a perfect hash function. Luckily, we do not need the hash function to be perfect to still gain performance efficiency.

# Example of hashing string values: 

We will use the sum of the ordinal value of each letter of the string. Then find the remainder when divide by the table size to get the hash value

Ordinal value example:

```python
>>> ord('c')
99
>>> ord('a')
97
>>> ord('t')
116

```

Hashing Function:
```python
def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])

    return sum%tablesize

```
# Implementation in python 

One of the most useful Python collections is the dictionary. Recall that a dictionary is an associative data type where you can store key–data pairs. The key is used to look up the associated data value. We often refer to this idea as a map.

The map abstract data type is defined as follows. The structure is an unordered collection of associations between a key and a data value. The keys in a map are all unique so that there is a one-to-one relationship between a key and a value. The operations are given below.

Map() Create a new, empty map. It returns an empty map collection.

put(key,val) Add a new key-value pair to the map. If the key is already in the map then replace the old value with the new value.

get(key) Given a key, return the value stored in the map or None otherwise.

del Delete the key-value pair from the map using a statement of the form del map[key].

len() Return the number of key-value pairs stored in the map.

in Return True for a statement of the form key in map, if the given key is in the map, False otherwise.

One of the great benefits of a dictionary is the fact that given a key, we can look up the associated data value very quickly. In order to provide this fast look up capability, we need an implementation that supports an efficient search. We could use a list with sequential or binary search but it would be even better to use a hash table as described above since looking up an item in a hash table can approach O(1) performance

# Read more at 

https://runestone.academy/runestone/books/published/pythonds/SortSearch/Hashing.html