# Binary Tree

A tree whose elements have at most 2 children is called a binary tree. Since each element in a binary tree can have only 2 children, we typically name them the left and right child.

A Binary Tree node contains following parts.

__1. Data__

__2. Pointer to left child__

__3. Pointer to right child__

# Why tree?

1. One reason to use trees might be because you want to store information that naturally forms a hierarchy. For example, the file system on a computer: 
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
2. Trees (with some ordering e.g., BST) provide moderate access/search (quicker than Linked List and slower than arrays). 
3. Trees provide moderate insertion/deletion (quicker than Arrays and slower than Unordered Linked Lists). 
4. Like Linked Lists and unlike Arrays, Trees don’t have an upper limit on number of nodes as nodes are linked using pointers.
Main applications of trees include: 
1. Manipulate hierarchical data. 
2. Make information easy to search (see tree traversal). 
3. Manipulate sorted lists of data. 
4. As a workflow for compositing digital images for visual effects. 
5. Router algorithms 
6. Form of a multi-stage decision-making (see business chess). 

## Basic Tree implementation python

```python

# Python program to introduce Binary Tree
 
# A class that represents an individual node in a
# Binary Tree
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
 
 
# create root
root = Node(1)
''' following is the tree after above statement
        1
      /   \
     None  None'''
 
root.left      = Node(2);
root.right     = Node(3);
   
''' 2 and 3 become left and right children of 1
           1
         /   \
        2      3
     /    \    /  \
   None None None None'''
 
 
root.left.left  = Node(4);
'''4 becomes left child of 2
           1
       /       \
      2          3
    /   \       /  \
   4    None  None  None
  /  \
None None'''

```
## Source: 

https://www.geeksforgeeks.org/binary-tree-set-1-introduction/

## Important Concepts in Tree

Please follow these [Hackerrank problems](https://www.hackerrank.com/domains/data-structures?filters%5Bsubdomains%5D%5B%5D=trees&filters%5Bsubdomains%5D%5B%5D=balanced-trees) to learn important concepts such as Traversals, Inversion, Lowest Ancestor,etc.

My solutions to these problems :

[C++](https://github.com/acao2002/Learn-DataStructures-and-Algorithms-with-Hackerrank-Solutions/tree/main/Data%20Structures%20Problems(C%2B%2B)/Tree)

[Python](https://github.com/acao2002/Learn-DataStructures-and-Algorithms-with-Hackerrank-Solutions/tree/main/Data%20Structures%20Problems(python)/Tree)