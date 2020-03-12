# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        conn = collections.defaultdict(list)
        def connect(parent, child):
            if parent and child:
                conn[parent.val].append(child.val)
                conn[child.val].append(parent.val)
            if child.left: connect(child, child.left)
            if child.right: connect(child, child.right)
        connect(None, root)
        # BFS
        queue = collections.deque()
        queue.append(target.val)
        visited = set([target.val])
        for k in range(K):
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                for j in conn[node]:
                    if j not in visited:
                        queue.append(j)
                        visited.add(j)
        return list(queue)