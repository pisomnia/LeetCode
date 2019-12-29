class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split('/')
        stack = []
        for i in path:
            if i == '..':
                if len(stack):
                    stack.pop()
            elif i != '.' and i != '':
                stack.append(i)
        return '/' + '/'.join(stack)