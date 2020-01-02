class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for ast in asteroids:
            while stack and ast < 0 and stack[-1] >= 0:
                pre = stack.pop()
                if ast == -pre:
                    ast = None
                    break
                elif -ast < pre:
                    ast = pre
            if ast != None:
                stack.append(ast)
        return stack
