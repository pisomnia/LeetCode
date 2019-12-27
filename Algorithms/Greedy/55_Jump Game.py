class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<1:
            return False
        if len(nums)==1:
            return True
        last_pos=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if (nums[i]+i)>=last_pos:
                last_pos=i
        return last_pos==0