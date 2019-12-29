class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res=[-1]*len(nums1)
        stack=[]
        for i in range(len(nums2)):
            while stack and stack[-1]<nums2[i]:
                if stack[-1] in nums1:
                    res[nums1.index(stack[-1])]=nums2[i]
                stack.pop()
            stack.append(nums2[i])
        return res