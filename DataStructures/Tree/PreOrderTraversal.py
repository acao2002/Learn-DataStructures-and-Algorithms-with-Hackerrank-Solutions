def preOrder(root):
    if root is not None:
        print(root.info, end = ' ')
        preOrder(root.left)
        preOrder(root.right)