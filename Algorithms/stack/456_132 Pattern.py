class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stk = [-sys.maxint]
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < stk[-1]:
                return True
            else:
                while stk and nums[i] > stk[-1]:
                    v = stk.pop()
                stk.append(nums[i])
                stk.append(v)
        return False