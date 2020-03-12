from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        
        res = []
        self.levelOrder(root, 0, res)
        return [level[-1] for level in res]

    def levelOrder(self, root, level, res):
        if not root: return
        if len(res) == level: 
            res.append([])
        res[level].append(root.val)
        if root.left: self.levelOrder(root.left, level + 1, res)
        if root.right: self.levelOrder(root.right, level + 1, res)
        
        res = []
        if not root: return res
        queue = collections.deque()
        queue.append(root)
        while queue:
            res.append(queue[-1].val)
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res
        """
        if not root:
            return []
        stack=[]
        stack.append((root,0))
        res=[]
        while stack:
            cur,level=stack.pop()
            if level==len(res):
                res.append(cur.val)
            if cur.left:
                stack.append((cur.left,level+1))
            if cur.right:
                stack.append((cur.right,level+1))
        return res
