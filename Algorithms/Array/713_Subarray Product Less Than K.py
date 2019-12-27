class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        product = 1
        i = 0
        result = 0
        for j, num in enumerate(nums):
            product *= num 
            
            while i <= j and product >= k:
                product //= nums[i]
                i += 1 
                
            result += j - i + 1 
            #以j为右边界的subarray总数
        return result