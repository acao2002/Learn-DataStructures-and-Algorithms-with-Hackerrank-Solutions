# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def compare_lists(llist1, llist2):
    result = 0 
    if llist1 is None or llist2 is None:
        if llist1 is None and llist2 is None:
            result = 1
        else:
            result = 0
    elif (llist1.data == llist2.data):
        result = compare_lists(llist1.next,llist2.next)
    else:
        result = 0
        
    return result
     