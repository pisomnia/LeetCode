class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        res=[-1]*len(nums)
        stack=[]
        for i in range(n*2):
            while stack and nums[i%n]>nums[stack[-1]]:
                res[stack[-1]]=nums[i%n]
                stack.pop()
            stack.append(i%n)
        return res
