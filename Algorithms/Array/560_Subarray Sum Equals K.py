class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or len(nums)==0:
            return 0
        sum_num =[0]*len(nums)
        sum_num[0]=nums[0]

        for i in range(1,len(nums)):
            sum_num[i]=sum_num[i-1]+nums[i]
        res=0
        dic={}
        dic[0]=1
        for i in range(len(sum_num)):
            if (sum_num[i]-k) in dic:
                res+=dic[sum_num[i]-k]
            dic[sum_num[i]]=dic.get(sum_num[i],0)+1
        return res