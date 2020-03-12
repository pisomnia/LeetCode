# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
      
        if not root:
            return []
        result,current=[],[root]
        while current:
            next_level,vals=[],[]
            for node in current:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current=next_level
            result.append(vals)
        return result[::-1]
        """
        stack=[(root,0)]
        res=[]
        while stack:
            node,level=stack.pop()
            if node:
                if len(res)<level+1:
                    res.insert(0,[])
                res[-(level+1)].append(node.val)
                stack.append((node.right,level+1))
                stack.append((node.left,level+1))
        return res
