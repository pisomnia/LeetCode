# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head=ListNode(0)
        tmp=head
        rev=0
        while True:
            if l1:
                rev+=l1.val
                l1=l1.next
            if l2:
                rev+=l2.val
                l2=l2.next
            tmp.val=rev%10
            rev=rev/10
            if l1 or l2 or rev:
                tmp.next=ListNode(0)
                tmp=tmp.next
            else:
                break
        return head