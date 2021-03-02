""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def left(root, data):
    if not root:
        return True 
    if root.data >= data:
        return False
    
    return left(root.left, data) and left(root.right, data) and left(root.left, root.data) and right(root.right, root.data )


def right(root, data):
    if not root:
        return True 
    if root.data <= data:
        return False
    
    return right(root.right, data) and right(root.left, data) and right(root.right, root.data) and left(root.left, root.data)

        
        
def check_binary_search_tree_(root):
    return  left(root.left, root.data) and right(root.right, root.data)
    
    