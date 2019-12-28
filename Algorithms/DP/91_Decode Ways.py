class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=='' or s[0]=='0':
            return 0
        dp=[0]*(len(s)+1)
        dp[0]=1
        dp[1]=1
        
        for i in range(1,len(s)):
            if s[i]!='0' and 10<=int(s[i-1:i+1])<=26:
                dp[i+1]=dp[i]+dp[i-1]
            elif s[i]!='0':
                dp[i+1]=dp[i]
            elif 10<=int(s[i-1:i+1])<=26:
                dp[i+1]=dp[i-1]
            else:
                dp[i+1]=0
        return dp[-1]