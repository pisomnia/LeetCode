# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None:
            return head
        cur = head
        size = 1
        while cur.next!=None:
            size += 1
            cur = cur.next
        k = k%size
        if k==0:
            return head
        len = 1
        cur = head
        while len<size-k:
            len += 1
            cur = cur.next
        newHead = cur.next
        cur.next = None
        cur = newHead
        while cur.next!=None:
            cur = cur.next
        cur.next = head
        return newHead