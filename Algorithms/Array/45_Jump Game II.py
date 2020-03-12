class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return 0
        maxNext=0
        curMax=0
        res=0
        for i in range(len(nums)-1):
            maxNext=max(maxNext,i+nums[i])
            if i==curMax:
                res+=1
                curMax=maxNext
        return res