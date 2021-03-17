#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def deleteNode(head, position):
    p = head ;
    if position == 0:
        head = head.next
    else:
        for i in range(0,position-1):
            p = p.next 
        p.next = p.next.next 
    return head