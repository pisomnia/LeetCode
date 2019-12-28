class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num=0
        str={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in range(len(s)-1):
            if str[s[i]]<str[s[i+1]]:
                num-=str[s[i]]
            else:
                num+=str[s[i]]
        num+=str[s[-1]]
        return num