class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s)==0:
            return ''
        n=len(s)
        res=0
        dp=[[False for i in range(n)] for j in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if i==j:
                    dp[i][j]=True
                elif s[i]==s[j] and j-i<=2:
                    dp[i][j]=True
                elif s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j]=True
                if dp[i][j]:
                    if (j-i+1)>res:
                        res=j-i+1
                        left=i
                        right=j+1
        return s[left:right]
        