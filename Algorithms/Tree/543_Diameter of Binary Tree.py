# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res=[0]
        self.dfs(root,res)
        return res[0]
    
    def dfs(self,root,depth):
        if not root:
            return 0
        left=self.dfs(root.left,depth)
        right=self.dfs(root.right,depth)
        depth[0]=max(depth[0],left+right)
        return (1+max(left,right))

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.depth=0
        self.helper(root)
        return (self.depth)
        
        
    def helper(self,root):
        if not root:
            return 0
        left=self.helper(root.left)
        right=self.helper(root.right)
        self.depth=max(self.depth,left+right)
        return (1+max(left,right))