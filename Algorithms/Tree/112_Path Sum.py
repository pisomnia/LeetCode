# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        
        if not root:
            return False
        de=[(root,sum-root.val),]
        while de:
            node,curr_sum=de.pop()
            if not node.left and not node.right and curr_sum==0:
                return True
            if node.left:
                de.append((node.left,curr_sum-node.left.val))
            if node.right:
                de.append((node.right,curr_sum-node.right.val))
        return False
        """
        if root == None:
            return False
        if root.left == None and root.right == None:
            return root.val == sum
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)