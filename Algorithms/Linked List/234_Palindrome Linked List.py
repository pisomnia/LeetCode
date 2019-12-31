# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        rev=None
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        if fast!=None:
            slow=slow.next
        Node=None
        while slow!=None:
            temp=slow
            slow=slow.next
            temp.next=Node
            Node=temp

        while Node!=None:
            if Node.val==head.val:
                Node=Node.next
                head=head.next
            else:
                return False
        return True