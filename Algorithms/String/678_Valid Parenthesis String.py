class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        left, cp = 0, 0
        for i in range(0, n):
            if s[i] == '(':
                left += 1
                cp += 1
            elif s[i] == '*':
                if left > 0:
                    left -= 1
                cp += 1
            else:
                if left > 0:
                    left -= 1
                cp -= 1
                if cp < 0:
                    return False
        
        if left > 0:
            return False
        else:
            return True