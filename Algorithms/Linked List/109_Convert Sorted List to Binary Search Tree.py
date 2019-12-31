# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def findMid(head):
            slow=fast=head
            prev=None
            while fast and fast.next:
                prev=slow
                slow=slow.next
                fast=fast.next.next
            prev.next=None
            return slow
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        mid=findMid(head)
        root=TreeNode(mid.val)
        root.left=self.sortedListToBST(head)
        root.right=self.sortedListToBST(mid.next)
        
        return root
