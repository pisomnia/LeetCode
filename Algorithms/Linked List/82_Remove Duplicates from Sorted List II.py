# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:  
            return head  
  
        dummy = ListNode(-1)  
        dummy.next = head  
        prev = dummy 
        cur = head  
        while cur!=None and cur.next!=None:   ### check cur.next None  
            if cur.val == cur.next.val:  
                val = cur.val  
                while cur!=None and cur.val==val: ### check cur None  
                    cur = cur.next  
                prev.next = cur  
            else:  
                cur = cur.next  
                prev = prev.next  
        return dummy.next 