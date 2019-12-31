# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        slow=head
        fast=head
        while fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next
        mid=slow.next
        slow.next=None
        return self.merge(self.sortList(head),self.sortList(mid))
        
        
    def merge(self,l1,l2):
        dummy=ListNode(0)
        cur=dummy
        while l1 and l2:
            if l1.val<l2.val:
                cur.next=l1
                l1=l1.next
            else:
                cur.next=l2
                l2=l2.next
            cur=cur.next
        if l1:
            cur.next=l1
        if l2:
            cur.next=l2
        return dummy.next