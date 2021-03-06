"""
 Merge two linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


def CompareLists(headA, headB):
    if headA is None and headB is None:
        return 1 #Both are empty

    while headA is not None:
        if headB is None: #A is bigger than B (beause B ended)
            return 0

        if headA.data != headB.data:
            return 0

        headA = headA.next
        headB = headB.next

    if headB is not None:
        return 0 #B is bigger than A (We finished a but B still has items)

    return 1