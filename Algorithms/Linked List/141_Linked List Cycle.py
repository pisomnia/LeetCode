# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        
        nodeSet=set()
        while head:
            if head in nodeSet:
                return True
            else:
                nodeSet.add(head)
                head=head.next
        return False
        """
        if head is None:    		
            return False		
        p1 = head		
        p2 = head		
        while True:
            if p1.next is not None:
                p1=p1.next.next
                p2=p2.next
                if p1 is None or p2 is None:
                    return False
                elif p1 == p2:
                    return True
            else:
                return False