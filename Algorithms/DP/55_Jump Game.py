class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp=[False]*len(nums)
        dp[0]=True
        for i in range(1,len(nums)):
            for j in range(i):
                if dp[j] and (j+nums[j])>=i:
                    dp[i]=True
                    break
        return dp[-1]