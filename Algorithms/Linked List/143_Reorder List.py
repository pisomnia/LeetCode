# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        先找到中点，然后把后半段倒过来，然后前后交替合并
        """
        if None == head or None == head.next:
            return head

        fast = head
        slow = head
        
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        fast = slow.next
        slow.next = None
        
        p = fast.next
        fast.next = None
        while p:
            temp = p.next
            p.next = fast
            fast = p
            p = temp

        tail = head
        while fast:
            p = fast.next
            fast.next = tail.next
            tail.next = fast
            tail = tail.next.next
            fast = p
        return head