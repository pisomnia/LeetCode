import sys
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        if not nums or len(nums)<=2:
            return 
        res=sys.maxsize
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            while left<right:
                cur=nums[i]+nums[left]+nums[right]
                if abs(res-target)>abs(cur-target):
                    res=cur
                if (nums[left]+nums[right])==target-nums[i]:
                    return cur
                elif (nums[left]+nums[right])<target-nums[i]:
                    left+=1
                else:
                    right-=1
        return res