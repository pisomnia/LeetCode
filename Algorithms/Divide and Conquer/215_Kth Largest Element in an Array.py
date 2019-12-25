import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        nums=[-i for i in nums]
        heapq.heapify(nums)
        if k==1:
            return -1*heapq.heappop(nums)
        for i in range(k-1):
            heapq.heappop(nums)
        return -1*heapq.heappop(nums)
        """
        mid = nums[len(nums)//2]
        nums1=[]
        nums2=[]
        for num in nums:
            if num>mid:
                nums1.append(num)
            if num<mid:
                nums2.append(num)
        if k<=len(nums1):
            return self.findKthLargest(nums1,k)
        if k>len(nums)-len(nums2):
            return self.findKthLargest(nums2,k-(len(nums)-len(nums2)))
        return mid