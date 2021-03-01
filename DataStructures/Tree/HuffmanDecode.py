import queue as Queue

"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""        

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
    p = root
    for i in s:
        if i == "0":
            p = p.left
            if p.left is None and p.right is None:
                print(p.data, end = "")
                p = root
        else:
            p = p.right
            if p.left is None and p.right is None:
                print(p.data, end = "")
                p = root


