# Complete the getNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def getNode(head, positionFromTail):
    count = 0
    result = head 
    current = head 
       
    while current is not None:    
        current = current.next   
       
        if count > positionFromTail:
            result = result.next
        count += 1      
    return result.data
