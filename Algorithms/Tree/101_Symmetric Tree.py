# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root,root)
        
    
    def helper(self,t1,t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        if t1.val!=t2.val:
            return False
        return self.helper(t1.left,t2.right) and self.helper(t1.right,t2.left)