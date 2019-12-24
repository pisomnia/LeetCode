# Multiply the numbers in the left first then multiply the right numbers
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        
        res  = [1 for i in nums]
        left = 1
        right = 1
        n=len(nums)
        for i in range(n):
            res[i]*=left
            left*=nums[i]
        for j in reversed(range(n)):
            res[j]*=right
            right*=nums[j]
        return res