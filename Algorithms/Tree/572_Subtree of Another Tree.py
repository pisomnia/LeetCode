# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not t:
            return True
        if not s:
            return False
        if self.helper(s,t):
            return True
        left=self.isSubtree(s.left,t)
        right=self.isSubtree(s.right,t)
        return left or right
    
    def helper(self,s,t):
        if not s:
            return t is None
        if t is None:
            return False
        if s.val!=t.val:
            return False
        return self.helper(s.left,t.left) and self.helper(s.right,t.right)