# Data Structures and Algorithms(DSAs)

Data Structures are tools that we use to manage and organize data. Algorithms are specific steps that we take to arrive at a particular solution. DSAs are important concepts for programming and are often used in complex applications and tested in techinical interviews for software engineering positions. 

DSAs can be hard to navigate being a self-learner or new in coding in general. As someone who is going the process of self-studying DSAs, I decide to put together this github repository, where I corroborate my own understanding and different sources(that I used) to write up short introductions and tutorials for these concepts. 

In addition to explaning the theory, I have also included my solutions of [Hackerrank DSAs problems](https://www.hackerrank.com/domains/data-structures), which are sorted into each category(linkedlist, trees, dynamic programming, etc..). Hackerrank problems are great for beginners to follow each concept and learn its operations. They also rank you among Hackerrank coders, which somewhat gives you the motivation to grind I guess :). 

Below is an index of this repository, which, I hope, would help you navigate through my collections and somewhat help you with your DSA grinding journey! 

# Data Structures


1. Linked List 

A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations. The elements in a linked list are linked using pointers

```
node1 --> node2 --> node3 --> node4 --> node 5 --> null
```
- [LinkedList Introduction](https://github.com/acao2002/Learn-DataStructures-and-Algorithms-with-Hackerrank-Solutions/tree/main/Learn%20Data%20Structures/LinkedList)
- [Hackerrank problems](https://www.hackerrank.com/domains/data-structures?filters%5Bsubdomains%5D%5B%5D=linked-lists)
- [Hackerrank solutions in Python]()
- [Hackerrank solutions in C++](https://github.com/acao2002/Learn-DataStructures-and-Algorithms-with-Hackerrank-Solutions/tree/main/Data%20Structures%20Problems(C%2B%2B))

2. Tree

```
file system
-----------
     /    <-- root
  /      \
...       home
      /          \
   ugrad        course
    /       /      |     \
  ...      cs101  cs112  cs113
```

A tree data structure can be defined recursively as a collection of nodes (starting at a root node), where each node is a data structure consisting of a value, together with a list of references to nodes (the "children"), with the constraints that no reference is duplicated, and none points to the root.

- [Tree Introduction](https://github.com/acao2002/Learn-DataStructures-and-Algorithms-with-Hackerrank-Solutions/tree/main/Learn%20Data%20Structures/Tree)
- [Binary Heap](https://github.com/acao2002/Learn-DataStructures-and-Algorithms-with-Hackerrank-Solutions/tree/main/Learn%20Data%20Structures/Priority%20Queues)
- [Hackerrank problems](https://www.hackerrank.com/domains/data-structures?filters%5Bsubdomains%5D%5B%5D=balanced-trees&filters%5Bsubdomains%5D%5B%5D=trees)
- [Hackerrank solutions in Python](https://github.com/acao2002/Learn-DataStructures-and-Algorithms-with-Hackerrank-Solutions/tree/main/Data%20Structures%20Problems(python))
- [Hackerrank solutions in C++](https://github.com/acao2002/Learn-DataStructures-and-Algorithms-with-Hackerrank-Solutions/tree/main/Data%20Structures%20Problems(C%2B%2B))

3. Stack and Queue 

```                     
                                STACK                                                   QUEUE
                                out                                                     out
                                 |                                                      |
                                 v                                                      v
                    [0,1,2,3,4,5,6]                                        [0,1,2,3,4,5,6]
                                 ^                                         ^
                                 |                                         |
                                 in                                        in
```

 **A stack** is a linear data structure in which elements can be inserted and deleted only from one side of the list, called the top. ... The queue data structure follows the FIFO (First In First Out) principle, i.e. the element inserted at first in the list, is the first element to be removed from the list.

 **A queue** is a linear data structure in which elements can be inserted only from one side of the list called rear, and the elements can be deleted only from the other side called the front. The queue data structure follows the FIFO (First In First Out) principle

- [Stack and Queue](https://github.com/acao2002/Learn-DataStructures-and-Algorithms-with-Hackerrank-Solutions/tree/main/Learn%20Data%20Structures/Queues%20and%20Stacks)
- [Hackerrank problems](https://www.hackerrank.com/domains/data-structures?filters%5Bsubdomains%5D%5B%5D=stacks&filters%5Bsubdomains%5D%5B%5D=queues)
- [Hackerrank solutions in Python](https://github.com/acao2002/Learn-DataStructures-and-Algorithms-with-Hackerrank-Solutions/tree/main/Data%20Structures%20Problems(python))
- [Hackerrank solutions in C++](https://github.com/acao2002/Learn-DataStructures-and-Algorithms-with-Hackerrank-Solutions/tree/main/Data%20Structures%20Problems(C%2B%2B))

4. HashTable

In computing, a hash table (hash map) is a data structure that implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index, also called a hash code, into an array of buckets or slots, from which the desired value can be found.

- [Hashing and Hash functions](https://github.com/acao2002/Learn-DataStructures-and-Algorithms-with-Hackerrank-Solutions/tree/main/Learn%20Data%20Structures/HashTable)

5. Array 
```
[0,1,2,3,4,5,5,6,6,7,7,4]
```
An array is a data structure, which can store a fixed-size collection of elements of the same data type. ... An array is used to store a collection of data, but it is often more useful to think of an array as a collection of variables of the same type.

- [Hackerrank problems](https://www.hackerrank.com/domains/data-structures?filters%5Bsubdomains%5D%5B%5D=arrays)
- [Hackerrank solutions in Python](https://github.com/acao2002/Learn-DataStructures-and-Algorithms-with-Hackerrank-Solutions/tree/main/Data%20Structures%20Problems(python))

6. Heap 
- [Binary Heap](https://github.com/acao2002/Learn-DataStructures-and-Algorithms-with-Hackerrank-Solutions/tree/main/Learn%20Data%20Structures/Priority%20Queues)
- [Hackerrank Problems](https://www.hackerrank.com/domains/data-structures?filters%5Bsubdomains%5D%5B%5D=heap)
- [Solutions in Python](https://github.com/acao2002/Learn-DataStructures-and-Algorithms-with-Hackerrank-Solutions/tree/main/Data%20Structures%20Problems(python)/Heap)
- [Solutions in c++](https://github.com/acao2002/Learn-DataStructures-and-Algorithms-with-Hackerrank-Solutions/tree/main/Data%20Structures%20Problems(C%2B%2B)/Heap)

# Algorithms 

1. Sorting algorithms 

- [Insertion Sort](https://github.com/acao2002/Learn-DataStructures-and-Algorithms-with-Hackerrank-Solutions/tree/main/LearnAlgorithms/Sorting%20Algorithms/InsertionSort)
- [Merge Sort](https://github.com/acao2002/Learn-DataStructures-and-Algorithms-with-Hackerrank-Solutions/tree/main/LearnAlgorithms/Sorting%20Algorithms/MergeSort)
- [Quick Sort](https://github.com/acao2002/Learn-DataStructures-and-Algorithms-with-Hackerrank-Solutions/tree/main/LearnAlgorithms/Sorting%20Algorithms/QuickSort)
- [Counting Sort](https://github.com/acao2002/Learn-DataStructures-and-Algorithms-with-Hackerrank-Solutions/tree/main/LearnAlgorithms/Sorting%20Algorithms/CountingSort)
- [Hackerrank problems](https://www.hackerrank.com/domains/algorithms?filters%5Bsubdomains%5D%5B%5D=arrays-and-sorting)
- [python solutions](https://github.com/acao2002/Learn-DataStructures-and-Algorithms-with-Hackerrank-Solutions/tree/main/Algorithms%20Problems/Sorting)

2. Hashing 

- [Hashing and Hash functions](https://github.com/acao2002/Learn-DataStructures-and-Algorithms-with-Hackerrank-Solutions/tree/main/Learn%20Data%20Structures/HashTable)

3. Search algorithms 

- [Search algorithms](https://github.com/acao2002/Learn-DataStructures-and-Algorithms-with-Hackerrank-Solutions/tree/main/LearnAlgorithms/Search)

4. Dynamic programming 

- [Dynamic programming](https://github.com/acao2002/Learn-DataStructures-and-Algorithms-with-Hackerrank-Solutions/tree/main/LearnAlgorithms/DynamicProgramming)
- [Hackerrank problems](https://www.hackerrank.com/domains/algorithms?filters%5Bsubdomains%5D%5B%5D=dynamic-programming)
- [python solutions](https://github.com/acao2002/Learn-DataStructures-and-Algorithms-with-Hackerrank-Solutions/tree/main/Algorithms%20Problems/Dynamic%20Programming)

5. Recursion 

I did not do any Recursion specific problems since I have been writing a lot of recursive solutions for **linked lists** and **trees**

Will include here later !!


