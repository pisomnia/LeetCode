# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        
        res=[]
        self.preorder(root,0,res)
        return res
    
    def preorder(self,root,depth,res):
        if not root:
            return
        if len(res)<depth+1:
            res.append([])
        res[depth].append(root.val)
        self.preorder(root.left,depth+1,res)
        self.preorder(root.right,depth+1,res)
        """
        res=[]
        if not root:
            return res
        queue=collections.deque()
        queue.append(root)
        while queue:
            res.append([node.val for node in queue])
            for i in range(len(queue)):
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res 