class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dp_max=[0]*len(nums)
        dp_min=[0]*len(nums)
        dp_max[0]=nums[0]
        dp_min[0]=nums[0]
        for i in range(1,len(nums)):
            dp_max[i]= max(dp_max[i-1]*nums[i],dp_min[i-1]*nums[i],nums[i])
            dp_min[i]= min(dp_max[i-1]*nums[i],dp_min[i-1]*nums[i],nums[i])
        return max(dp_max)