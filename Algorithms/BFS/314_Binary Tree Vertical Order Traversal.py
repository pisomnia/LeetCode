# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        results = collections.defaultdict(list)
        queue = deque()
        queue.append((root, 0))
        while queue:
            node, x = queue.popleft()
            if node:
                results[x].append(node.val)
                queue.append((node.left, x - 1))
                queue.append((node.right, x + 1))
                
        return [results[i] for i in sorted(results)]
