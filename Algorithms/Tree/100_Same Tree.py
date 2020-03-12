# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
    
        def check(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val==q.val:
                return True
            else:
                return False
        deq=deque([(p,q),])
        while deq:
            p,q=deq.popleft()
            if not check(p,q):
                return False
            if p:
                deq.append((p.left,q.left))
                deq.append((p.right,q.right))
        return True
        """
        if p==None and q==None:
            return True
        if p and q and p.val==q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        return False