class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        self.res=[]
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.twoSum(nums[i+1:],nums[i])
        return self.res
    def twoSum(self,nums,cur):
        hashmap=set()
        seen=set()
        for i in range(len(nums)):
            complement = 0-cur-nums[i]
            if nums[i] not in seen and complement in hashmap:
                seen.add(nums[i])
                self.res.append([cur,complement,nums[i]])
            else:
                hashmap.add(nums[i])