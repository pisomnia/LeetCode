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
        curNode = head
        size = 1
        while curNode!=None:
            size += 1
            curNode = curNode.next
        size -= 1
        k = k%size
        if k==0:
            return head
        len = 1
        curNode = head
        while len<size-k:
            len += 1
            curNode = curNode.next
        newHead = curNode.next
        curNode.next = None
        curNode = newHead
        while curNode.next!=None:
            curNode = curNode.next
        curNode.next = head
        return newHead