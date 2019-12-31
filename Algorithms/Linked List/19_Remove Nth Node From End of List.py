# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        res=ListNode(0)
        res.next=head
        fast=head
        slow=res
        for i in range(n):
            fast=fast.next
        while fast:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return res.next