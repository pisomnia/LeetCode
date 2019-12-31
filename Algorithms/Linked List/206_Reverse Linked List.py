# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        cur=head
        prev=None
        while cur!=None:
            tmp=cur.next
            cur.next=prev
            prev=cur
            cur=tmp            
        return prev


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        递归
        """
        return self.reverse(head, None)
        
    def reverse(self, head, newHead):
        if not head:
            return newHead
        headnext = head.next
        head.next = newHead
        return self.reverse(headnext, head)
