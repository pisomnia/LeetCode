class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hashmap={"(":")","[":"]","{":"}"}
        stack=[]
        for c in s:
            if c in hashmap:
                stack.append(c)
            elif stack and c==hashmap[stack[-1]]:
                stack.pop()
            else:
                return False
        return not stack