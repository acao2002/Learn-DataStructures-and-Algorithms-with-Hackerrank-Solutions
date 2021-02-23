
# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    fast = head
    slow = head 
    
    while (fast is not None and slow is not None):
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return 1
    
    return 0
    