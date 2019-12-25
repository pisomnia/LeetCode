class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        left=self.findLeft(nums,target)
        right=self.findRight(nums,target)
        return [left,right]
        
    def findLeft(self,nums,target):
        left=0
        right=len(nums)-1
        while left<right:
            mid=left+(right-left)/2
            if (nums[mid]<target):
                left=mid+1
            else:
                right=mid
        if nums[left]!=target:
            return -1
        return left         
        
    def findRight(self,nums,target):
        left=0
        right=len(nums)-1
        while left<right:
            mid=left+(right-left+1)/2
            if (nums[mid]>target):
                right=mid-1
            else:
                left=mid
        if nums[left]!=target:
            return -1
        return left