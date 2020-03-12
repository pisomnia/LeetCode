class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 1
        num_set=set()
        for i in range(1,len(nums)+1):
            num_set.add(i)
        for i in range(len(nums)):
            if nums[i] in num_set:
                num_set.remove(nums[i])
        if not num_set:
            return len(nums)+1
        return min(num_set)