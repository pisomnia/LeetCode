class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if not s:
            return 0
        dp=[[False for j in range(len(s))] for i in range(len(s))]
        ans=0
        for i in range(len(s)-1,-1,-1):
            for j in range(i,len(s)):
                if s[i]==s[j] and (j-i<=2 or dp[i+1][j-1]==True):
                    dp[i][j]=True
                if dp[i][j]==True:
                    ans+=1
        return ans