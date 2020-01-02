class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        previ = 0
        res = ""
        count = 0
        for i, s in enumerate(S):
            if s == '(':
                count += 1
            else:
                count -= 1
            if count == 0:
                res += S[previ + 1: i]
                previ = i + 1
        return res
        