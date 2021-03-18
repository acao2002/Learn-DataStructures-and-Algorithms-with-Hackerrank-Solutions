# Binary Tree

A tree whose elements have at most 2 children is called a binary tree. Since each element in a binary tree can have only 2 children, we typically name them the left and right child.

A Binary Tree node contains following parts.

__1. Data__

__2. Pointer to left child__

__3. Pointer to right child__

# Why tree?

Why Trees? 
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