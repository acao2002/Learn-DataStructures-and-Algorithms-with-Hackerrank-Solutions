# Complete the removeDuplicates function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def removeDuplicates(head):
    p = head
    current = head
    if p.next is None:
        return current
    if p.next.data > p.data and p.next is not None:
        current.next = removeDuplicates(p.next)
        return current
    else:
        return removeDuplicates(p.next)
