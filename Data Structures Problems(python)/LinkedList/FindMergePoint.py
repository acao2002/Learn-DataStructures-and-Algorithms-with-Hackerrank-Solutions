
# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):
    p = head1
    p2 = head2
    while p != p2:
        if p.next is None:
            p = head2
        else:
            p = p.next
        if p2.next is None:
            p2 = head1
        else: 
            p2 = p2.next            
    return p.data
        