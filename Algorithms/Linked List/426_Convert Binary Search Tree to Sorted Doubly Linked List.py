"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root: return root
        first = None
        last = None
        prev = None
    	# iterate the tree like a list
        for v in self.inorder(root):
            if first is None: first = v
            last = v
            if prev is not None:
                prev.right = v
                v.left = prev
            prev = v
        first.left = last
        last.right = first
        return first
        
    def inorder(self, node):
        if not node: return
        left = node.left
        for n in self.inorder(left):
            yield n
        yield node
        right = node.right
        for n in self.inorder(right):
            yield n