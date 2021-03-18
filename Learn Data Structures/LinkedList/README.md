# LinkedList 

A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations. The elements in a linked list are linked using pointers 


## Analysis

**Advantages over arrays**

1) Dynamic size

2) Ease of insertion/deletion

**Drawbacks:**

1) Random access is not allowed. We have to access elements sequentially starting from the first node. So we cannot do binary search with linked lists efficiently with its default implementation. Read about it here.

2) Extra memory space for a pointer is required with each element of the list.

3) Not cache friendly. Since array elements are contiguous locations, there is locality of reference which is not there in case of linked lists.

## Simple LinkedList implementation (python)

```python 
# A simple Python program to introduce a linked list 
  
# Node class 
class Node: 
  
    # Function to initialise the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize next as null 
  
  
# Linked List class contains a Node object 
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
  
# Code execution starts here 
if __name__=='__main__': 
  
    # Start with the empty list 
    llist = LinkedList() 
  
    llist.head = Node(1) 
    second = Node(2) 
    third = Node(3) 
  
    ''' 
    Three nodes have been created. 
    We have references to these three blocks as head, 
    second and third 
  
    llist.head        second              third 
         |                |                  | 
         |                |                  | 
    +----+------+     +----+------+     +----+------+ 
    | 1  | None |     | 2  | None |     |  3 | None | 
    +----+------+     +----+------+     +----+------+ 
    '''
  
    llist.head.next = second; # Link first node with second  
  
    ''' 
    Now next of first Node refers to second.  So they 
    both are linked. 
  
    llist.head        second              third 
         |                |                  | 
         |                |                  | 
    +----+------+     +----+------+     +----+------+ 
    | 1  |  o-------->| 2  | null |     |  3 | null | 
    +----+------+     +----+------+     +----+------+  
    '''
  
    second.next = third; # Link second node with the third node 
  
    ''' 
    Now next of second Node refers to third.  So all three 
    nodes are linked. 
  
    llist.head        second              third 
         |                |                  | 
         |                |                  | 
    +----+------+     +----+------+     +----+------+ 
    | 1  |  o-------->| 2  |  o-------->|  3 | null | 
    +----+------+     +----+------+     +----+------+  
    '''
```

## LinkedList Concepts 

Please go through the [linked list problems on Hackerrank](https://www.hackerrank.com/domains/data-structures?filters%5Bsubdomains%5D%5B%5D=linked-lists)

As you go through the problems, you will be able to pick up small concepts like insertion, reversion, removal along the way!

You can also view my solutions in [python](https://github.com/acao2002/Learn-DataStructures-and-Algorithms-with-Hackerrank-Solutions/tree/main/Data%20Structures%20Problems(python)/LinkedList) and [C++](https://github.com/acao2002/Learn-DataStructures-and-Algorithms-with-Hackerrank-Solutions/tree/main/Data%20Structures%20Problems(C%2B%2B)/LinkedList) of these problems to learn about my approach to these problems