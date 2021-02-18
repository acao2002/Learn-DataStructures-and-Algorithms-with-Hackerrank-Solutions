# Complete the reversePrint function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reversePrint(head):
    rl = []
    while head is not None:
        rl.insert(0,head.data)
        head = head.next
    
    for x in rl:
        print(x)

