# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA, lenB = 0, 0
        node1, node2 = headA, headB
        while node1 is not None:
            lenA += 1
            node1 = node1.next
        while node2 is not None:
            lenB += 1
            node2 = node2.next
        
        node1, node2 = headA, headB
        while lenA > lenB:
            node1 = node1.next
            lenA -= 1
        while lenB > lenA:
            node2 = node2.next
            lenB -=1
        while node1 is not node2:
            node1 = node1.next
            node2 = node2.next
        return node1