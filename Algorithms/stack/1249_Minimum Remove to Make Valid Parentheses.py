class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        left_uncompair = []
        left_remove = {}
        right_remove = {}
        for i in range(len(s)):
            if s[i] == '(':
                left_uncompair.append(i)
                left_remove[i] = 1
            elif s[i] == ')':
                if len(left_uncompair) == 0:
                    right_remove[i] = 1
                else:
                    inx  = left_uncompair.pop(-1)
                    del left_remove[inx]

        res = ''
        for i in range(len(s)):
            if i in right_remove or i in left_remove:
                continue
            res += s[i]
        return res