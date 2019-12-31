# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return None
        slow = fast = head      	#初始化快指针和慢指针
        while fast and fast.next:	
            slow = slow.next
            fast = fast.next.next
            if fast == slow:		#快慢指针相遇
                break
        if slow == fast:
            slow = head				#从头移动慢指针
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow				#两指针相遇处即为环的入口
        return None