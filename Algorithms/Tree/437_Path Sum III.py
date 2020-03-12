# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        
        if not root:
            return 0
        
        def dfs(root,sum):
            count=0
            if not root:
                return 0
            if root.val==sum:
                count+=1
            count+=dfs(root.left,sum-root.val)
            count+=dfs(root.right,sum-root.val)
            return count
        return dfs(root,sum)+self.pathSum(root.left,sum)+self.pathSum(root.right,sum) 
        """
        #BFS + DFS
        res = [0]
        que = collections.deque()
        que.append(root)
        while que:
            node = que.popleft()
            if not node:
                continue
            self.dfs(node, res, 0, sum)
            que.append(node.left)
            que.append(node.right)
        return res[0]
    
    def dfs(self, root, res, path, target):
        if not root:
            return
        if root.val == target:
            res[0] += 1
        self.dfs(root.left, res, path, target-root.val)
        self.dfs(root.right, res, path, target-root.val)