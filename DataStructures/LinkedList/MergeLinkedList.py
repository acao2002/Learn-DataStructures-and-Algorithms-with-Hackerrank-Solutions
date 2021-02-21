def mergeLists(headA, headB):
  if headA is None and headB is None:
    return None
  
  if headA is None:
    return headB

  if headB is None:
    return headA
  
  if headA.data < headB.data:
    
    headA.next = mergeLists(headA.next, headB)
    return headA
  else:
    
    headB.next = mergeLists(headA, headB.next)
    return headB