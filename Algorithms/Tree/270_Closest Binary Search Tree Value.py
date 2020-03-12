# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        
        self.res=float('inf')
        self.dfs(root,target)
        return self.res
    
    def dfs(self,root,target):
        if not root:
            return 
        if abs(target-self.res)>abs(target-root.val):
            self.res=root.val
        if target>root.val:
            self.dfs(root.right,target)
        else:
            self.dfs(root.left,target)
        