  
# Complete the reverse function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reverse(head):
    
    if head is None or head.next is None:
        return head 
    else:
        remaining = reverse(head.next)
        head.next.next = head
        head.next = None
        return remaining