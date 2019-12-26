class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int

        """
        if not nums or len(nums)==0:
            return 0
        minLength=len(nums)+1
        sum=0
        left=0
        for right in range(len(nums)):
            sum+=nums[right]
            while left<=right and sum>=s:
                sum-=nums[left]
                minLength=min(minLength,right-left+1)
                left+=1
        if minLength==len(nums)+1:
            return 0
        return minLength