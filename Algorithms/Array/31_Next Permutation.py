class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 先找第一个nums[i]<nums[i+1],然后跟nums[i]右侧比它大的数中的最小值对换，把nums[i]右侧的整个列表翻转
        if not nums or len(nums)==0:
            return 
        n=len(nums)
        small=-1
        big=-1
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                small=i
                break
        if small ==-1:
            nums.reverse()
            return nums
        for i in range(n-1,small,-1):
            if nums[i]>nums[small]:
                big=i
                break
        nums[small],nums[big] = nums[big],nums[small]
        for i in range(0,(n-small)//2):
            nums[small+1+i],nums[n-1-i]=nums[n-1-i],nums[small+1+i]
        return nums