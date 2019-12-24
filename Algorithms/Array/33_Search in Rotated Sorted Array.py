class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)<0:
            return -1
        if len(nums)==1:
            return 0 if nums[0]==target else -1
        return self.helper(nums,target)
        
    def helper(self,nums,target):
        left=0
        right=len(nums)-1
        while left<=right:
            mid=left+(right-left)/2
            if nums[mid]==target:
                return mid
            if target>=nums[0]:
                if nums[mid]>=nums[0] and nums[mid]>target:
                    right=mid-1
                elif nums[mid]>=nums[0] and nums[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
                    
            else:
                if nums[mid]>=nums[0]:
                    left=mid+1
                elif nums[mid]<=nums[0] and nums[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
        return -1